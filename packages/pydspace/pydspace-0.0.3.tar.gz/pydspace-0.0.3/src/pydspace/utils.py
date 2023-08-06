import logging
import pandas as pd
import numpy as np

logger = logging.getLogger(__name__)

def is_string_column(series: pd.Series) -> bool:
    """
    Attempts to guess if the pandas series has actually as 'dtype' string.

    If 0.95 of the elements of the series have a string type then we declare the column as a
    string column.

    Args:
        series: The pd.Series column to check for.
    Returns:
        boolean
    """

    # This condition has to be meet.
    assert series.dtype == object or series.dtype == pd.StringDtype()

    # Check if the 95% of the data points are strings.
    N = len(series)
    counter = 0
    for item in series:
        if isinstance(item, str):
            counter += 1

    ratio = counter/N

    if ratio >= 0.95:
        return True
    else:
        return False 
