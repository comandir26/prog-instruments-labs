import re

from typing import Dict, List

import pandas as pd


def get_data(path_to_csv: str) -> pd.DataFrame:
    """
    This function reads the csv file in the specified path.

    Parameters:
        path_to_csv: str
          The path to the csv file

    Returns:
        data: pd.DataFrame
          The data from the сsv file
    """
    try:
        data = pd.read_csv(path_to_csv, sep=';', encoding='utf-16')
        return data
    except Exception as e:
        print(f'Error in reading the csv file: {e}')


def get_invalid_data(data: pd.DataFrame, patterns: Dict[str, str]) -> List[int]:
    """
    This function finds indexes of invalid rows in the data

    Parameters:
        data: pd.DataFrame
          Source data
        patterns: Dict[str, str]
          A dictionary in which the key is the column name and the value is
          a regular expression

    Returns:
        invalid_idx: List[int]
          List of invalid rows indexes
    """
    invalid_idx = pd.Index([])
    for column_name, regex in patterns.items():
        matches = data[column_name].str.match(regex, flags=re.IGNORECASE)
        idx_false = matches[matches==False].index
        invalid_idx = invalid_idx.append(idx_false)
    return invalid_idx.tolist()
 