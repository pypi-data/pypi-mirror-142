import matlab
import matlab.engine

# Type Definition
MatlabEngine = matlab.engine.matlabengine.MatlabEngine

# Start the Matlab Engine and save it as a constant
# for referencing it in other modules.
MATLAB_ENGINE = matlab.engine.start_matlab()

def get_matlab_engine() -> MatlabEngine:
    """
    Simple function that returns the already created matlab engine.
    """
    return MATLAB_ENGINE

def reset_matlab_engine() -> MatlabEngine:
    """
    Kills an existing matlab engine (if there is one) and creates another one that
    exposes for the others modules inside the package.
    """
    global MATLAB_ENGINE

    # Kill the already existing matlab engine
    MATLAB_ENGINE.quit()

    # Reassing in the global variable the new matlab engine
    MATLAB_ENGINE = matlab.engine.start_matlab()

    return MATLAB_ENGINE


# Avoid circular error
from .pydspace import dspace
