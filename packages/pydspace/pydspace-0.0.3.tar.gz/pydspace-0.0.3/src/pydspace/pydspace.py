import time
import matlab
import logging
import matlab.engine
import matlab.mlarray
import numpy as np
import pandas as pd
import sys

from typing import Union
from .utils import is_string_column
from . import get_matlab_engine

MatlabEngine = matlab.engine.matlabengine.MatlabEngine
SupportedType = Union[np.ndarray, pd.DataFrame]

logger = logging.getLogger(__name__)

class Dspace:
    """
    This class implements a wrapper for the objects that the
    MatlabEngine for python returns, when the user starts
    dSpace with pydspace.
    """

    def __init__(self, dsource, dspace_app, matlab_engine):
        self.dsource = dsource
        self.dspace_app = dspace_app
        self.matlab_engine = matlab_engine

    def dsource_info(self):
        """
        Prints, to the stdout that the associated engine has been started with,
        the info of the dsource object.
        """
        # TODO: Ideally 'info()' should return a string, so that we can handle
        # printing to the console or the loggin in pyton itself but it does
        # not. Instead the matlab code just prints to the console.
        self.matlab_engine.info(self.dsource, nargout=0)

    def add_data(self, *args):
        pass


def dspace(*args, path: str = None, no_gui: bool = False) -> Dspace:
    """
    This function its just a python rewrite of the dspace.m function provided
    in the dSpace matlab package. You can find more documentation in that
    respective file.

    Args:
        args: Either numpy arrays, or (name,value) pairs.
        path: Path of the directory where dspace is located.
    Returns:
        Matlab engine object.
    """
    input_names = []
    input_values = []

    num_args = len(args)
    i = 0
    while i < num_args:
        # Check if the arguments follow a (name, value) scheme and
        # proceed correspondingly.
        if isinstance(args[i], str):
            if i == num_args - 1 :
                error_msg = (
                    f"dspace: The last function input {i} is a string {args[i]}.\n"
                    "Strings can only occur in name, value pairs"
                    "(to give names to labels or features).\nInput ignored."

                )
                logger.warning(error_msg)
                break
                # raise ValueError(error_msg)

            name, value = args[i], args[i+1]

            # If the next argument is also an string, ignore those
            # two elements.
            if isinstance(value, str):
                error_msg = (
                    f"dspace: Function inputs {i} and {i+1} are both strings"
                    f" {name}, {value}.\n"
                    "Strings can only occur in name, value pairs"
                    "(to give names to labels or features).\nInput ignored."
                )
                i = i + 2
                logger.warning(error_msg)
                continue

            # Check if next argument is indeed a numpy array.
            # TODO: We must be able to use different dataypes not only
            # numpy arrays
            if not isinstance(value, np.ndarray):
                error_msg = (
                    f"dspace: Function input {i} is a string {name}.\n"
                    f"The next input must be a numpy.ndarray but is not.\n"
                    "Input ignored."
                )
                i = i + 2
                logger.warning(error_msg)
                continue

            # Create input from the name, value pair.
            # TODO: Make sure the name can be used in Matlab code.
            input_names.append(name)
            input_values.append(value)

            i = i + 2

        else:
            # TODO: In Matlab it is possible to get name of the variable
            # passed as argument to a function with 'inputname'. In Python
            # there is not a clean way to do this, therefore for the moment
            # if no names are passed, each value will get as name 'input_i'.
            name = f"name_{i}" 
            value = args[i]

            input_names.append(name)
            input_values.append(value)

            i = i + 1
    

    assert len(input_names) == len(input_values)

    # Start the Matlab Engine
    engine = get_matlab_engine()
    engine.addpath(path, nargout=0)


    # Perform the conversion from python objects to 'matlab.object'.
    for i, value in enumerate(input_values):
        input_values[i] = convert_value(value, engine)
        # Free the memory inmediatly
        del value


    # In the ideal case we would like to operate on the object
    # returned by the parseDspaceArgs matlab function, but the matlab api
    # for python does not allow it, so instead we just call the function and 
    # save the output in the workspace, then we use eval. An issue is that,
    # then the variable is a global one and not a local one, so naming bugs
    # could appear.
    # TODO: There might be a cleaner way to do this.

    engine.workspace["source_pydspace"] = engine.dspace.parseDspaceArgs(
        input_values,
        input_names,
        1,
        nargout = 1
    )

    instr_1 = "source_pydspace.createdBy = 'Import through dspace() function from python.';"
    instr_2 = "source_pydspace.createdOn = now();"

    engine.eval(instr_1, nargout=0)
    engine.eval(instr_2, nargout=0)

    source = engine.workspace["source_pydspace"]

    if no_gui:
        dsource = engine.dspace(source, nargout=1)
        dspace_app = None
    else:
        dsource, dspace_app = engine.dspace(source, nargout=2)

    # We must return the engine. Since we created it as a local 
    # variable if we don't return it, then it will just get deleted from the 
    # stack (i.e the engine gets killed the , and dspace will not open.

    # TODO: Maybe it's useful to also return the dspaceApp, dSource and the
    # dView
    dspace = Dspace(dsource, dspace_app, engine)

    return dspace

def convert_value(value: SupportedType, engine: MatlabEngine = None):
    if isinstance(value, np.ndarray):
        return convert_numpy_array(value)
    if isinstance(value, pd.DataFrame):
        return convert_dataframe(value, engine=engine)
    
def convert_numpy_array(array: np.ndarray) -> matlab.object:
    return matlab.double(array.tolist())

def convert_dataframe(df: pd.DataFrame, engine: MatlabEngine) -> matlab.object:
    """
    Takes a pandas DataFrame and attemps an as close as possible conversion to
    a matlab.Table, using the matlab engine for python. Unfortunately several
    hacks had to be performed to make this work. 

    Args: 
        df: DataFrame to convert to a matlab Table.
        engine: The MatlabEngine that provides the workspace where the Table will be stored.
    Returns:
        The matlab.object that references to the Table. 
    """
    # Pandas DataFrames returns scalars as numpy dtypes.
    # Numpy References:
    # https://numpy.org/doc/stable/reference/arrays.scalars.html#sized-aliases 
    # Matlab References
    # https://ch.mathworks.com/help/matlab/matlab_external/get-started-with-matlab-engine-for-python.html

    N = len(df)

    NUMERICAL_TYPE_CONVERSIONS = {
        np.float16: matlab.single, # There is no floa16 in the python api engine, so we use matlab.single.
        np.float32: matlab.single,
        np.float64: matlab.double,
        np.int8: matlab.int8,
        np.int16: matlab.int16,
        np.int32: matlab.int32,
        np.int64: matlab.int64,
        np.uint8: matlab.uint8,
        np.uint16: matlab.uint16,
        np.uint32: matlab.uint32,
        np.uint64: matlab.uint64,
        np.bool8: matlab.logical,
    }

    VALID_NUMERICAL_TYPES = list(NUMERICAL_TYPE_CONVERSIONS.keys())

    # First just get the valid columns.
    valid_columns = []
    for col_name, col_dtype in zip(df.columns, df.dtypes):
        if col_dtype in VALID_NUMERICAL_TYPES:
            valid_columns.append((col_name, col_dtype))
        elif isinstance(col_dtype, pd.StringDtype):
            valid_columns.append((col_name, col_dtype))
        elif is_string_column(df[col_name]):
            valid_columns.append((col_name, col_dtype))
            warn_msg = (
                f"Column {col_name} has a dtype 'object', however based on its items "
                "we infer a 'string' dtype"
            )
            logger.warning(warn_msg)
        else:
            # If it is not a string column then warn the user that the column it's skipped.
            error_msg = (
                f"Column {col_name} of the DataFrame has a dtype that is "
                "currently not supported. Skipping that column."
            )
            logger.warning(error_msg)


    # NOTE:
    # Unfortunately we cannot reshape matlab cells from python using the engine
    # (or at least I couldn't find a way to do it), and then continue to
    # reference the cell later in the python code. Each time you reference, in
    # python, a value that you have created with the matlab.engine, a type
    # conversion is created, and the reshape you have performed before is lost.
    # This issue forbids more short and clean ways to transform a DataFrame,
    # with supported columns, to a Matalab table, as for example.
    #     'table = engine.table(*input_values, "VariableNames", data.columns)'
    # sice the engine complains about the shape of the cells. If all the
    # columns of the DataFrame have only numerical data, then it is indeed
    # posible since you only work with mlarrays, but with columns with
    # text/categorial data, a cell must be created and the aforementioned issue
    # appears. Therefore we resort again to the use of 'engine.eval'.

    # We create an empty table in the global workspace.
    # Use time.time() to avoid possible global variable names bugs.
    table_var_name = f"local_table_{round(time.time())}"
    engine.workspace[table_var_name] = engine.table()

    mat_local_variables = []
    for col_name, col_dtype in valid_columns:
        col = df[col_name]
        var_name = f"local_{col_name}_{round(time.time())}"
        mat_local_variables.append(var_name)

        if col_dtype in VALID_NUMERICAL_TYPES:
            conversion_function = NUMERICAL_TYPE_CONVERSIONS[col_dtype.type]
            mat_col = conversion_function(col.tolist())
            mat_col.reshape((N, 1))

            logger.debug(f"From {col_dtype} to matlab.{conversion_function.__name__}.")

            engine.workspace[var_name] = mat_col

            instr = f"{table_var_name}.{col_name} = {var_name};"
            engine.eval(instr, nargout=0)
        else:
            # It must be a string a column, since we only support numerical and text data
            # from a pandas DataFrame.
            assert is_string_column(col) or isinstance(col_dtype, pd.StringDtype)

            mat_cell = engine.cell(col.tolist())
            engine.workspace[var_name] = mat_cell

            if isinstance(col_dtype, pd.StringDtype):
                logger.debug(f"From StringDtype to matlab cell of strings.")
            else:
                logger.debug(f"From {col_dtype} dtype to matlab.cell of strings.")

            instr_1 = f"{var_name} = reshape({var_name}, {N}, 1);"
            instr_2 = f"{table_var_name}.{col_name} = {var_name};"
            engine.eval(instr_1, nargout=0)
            engine.eval(instr_2, nargout=0)

    # Free the matlab memory by deleting the temporal variables created in the global
    # workspace.
    for mat_local_var in mat_local_variables:
        instr = f"clear {mat_local_var};"
        engine.eval(instr, nargout=0)

    return engine.workspace[table_var_name]


def add_feature(engine: matlab.engine, name: str) -> None:
    """
    Just a test function to see the capibilities of the eval function
    from the python matlab engine. THE DSPACE OBJECT MUST ALREADY EXISTS.

    Args:
        name: Name to indentify the new feature

    Returns:
        dsource.info string
    """

    # Transfer the numpy array to the already existing matlab workspace
    M = np.random.rand(1000, 28)
    engine.workspace["M"] = matlab.double(M.tolist())

    # Maybe do something like
    # send_matrix_to_matlab(engine, matrix, "name of the matrix for the matlab workspace")

    # Create instruction strings
    instr_feature_layout = "fl = dspace_features.FeatureLayout([1, 128], [], 1:128, [1, 128]);"
    instr_standard_features = f"f = dspace_features.StandardFeatures(M, '{name}', fl);"
    instr_add_features = "dsource.addFeatures(f);"

    # Make use of eval to add the feature to dsource
    engine.eval(instr_feature_layout, nargout=0)
    engine.eval(instr_standard_features, nargout=0)
    engine.eval(instr_add_features, nargout=0)

    engine.eval("dsource.info", nargout=0)


def send_matrix_to_matlab(engine: matlab.engine, matrix: np.ndarray, name_for_workspace: str) -> None:
    """
    TODO: Maybe not necessary.

    If a lot of methods using the engine are needed, it could be a
    good idea to wrap the matlab.engine object inside another engine
    class with all these functions as methods.
    """
    engine.workspace[name_for_workspace] = matlab.double(matrix.tolist())
