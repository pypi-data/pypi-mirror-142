import pandas as pd
import numpy as np
import warnings
from difflib import get_close_matches


"""
    File name: dataframes.py
    Author: Jacob Gerlach
    Description: Assortment of basic pandas DataFrame cleaning operations.
    Notes:
        * = Function has associated unit test.
"""


def read_spreadsheet(file, return_ext=False):

    # Get file MIME
    file_mime = file.content_type

    # Read CSV
    if file_mime == 'text/csv':
        file_ext = 'csv'

        # Read in data
        input_data = pd.read_csv(file)
        
    # Read TSV
    elif file_mime == 'text/tab-separated-values':
        file_ext = 'tsv'

        # Read in data
        input_data = pd.read_csv(file, sep='\t')
        
    # Read Excel
    elif (file_mime == 'application/vnd.ms-excel' or
        file_mime == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'):
        file_ext = 'xlsx'

        # Read in data
        input_data = pd.read_excel(file)

    # Unsupported filetype
    else:
        warnings.warn(f'"{file_mime}" is not a supported filetype.')


    return input_data, file_ext if return_ext else input_data

def drop_val(df, col_name, value):  # *
    """Drops row from df where column entry is equal to value.

    Args:
        df (pandas DataFrame): DataFrame containing rows to drop.
        col_name (str): Name of column to investigate.
        value (pandas object): Value to drop instances of.

    Returns:
        pandas DataFrame: DataFrame with rows dropped.
    """
    return pull_not_val(df, col_name, value).reset_index(drop=True)

def pull_val(df, col_name, value):  # *
    """Retrieves rows from df where column entry is equal to value.

    Args:
        df (pandas DataFrame): DataFrame containing rows to pull.
        col_name (str): Name of column to investigate.
        value (pandas object): Value to pull instances of.

    Returns:
        pandas DataFrame: DataFrame where value is found.
    """
    return df.where(df[col_name] == value).dropna()

def pull_not_val(df, col_name, value):  # *
    """Retrieves rows from df where column entry is not equal to value.

    Args:
        df (pandas DataFrame): DataFrame containing rows to pull.
        col_name (str): Name of column to investigate.
        value (pandas object): Value to not pull instances of.

    Returns:
        pandas DataFrame: DataFrame where value is not found.
    """
    return df.where(df[col_name] != value).dropna()


def id_nearest_col(df, name, case_insensitive=True):  # *
    """Sends closest column to input column name provided that it is at least 50% similar. CASE INSENSITIVE.

    Args:
        df (pandas DataFrame): DataFrame containing header with columns of interest.
        name (str): Column name to search for.
        case_insensitive (bool, optional): If True, converts both to lower before comparing. Defaults to True.

    Returns:
        str: Most similar column name.
    """
    similarity_ratio = 0.5  # 50%
    
    # Convert both to lowercase
    if case_insensitive:
        df_head = [col.lower() for col in df]
        name = name.lower()
    else:
        df_head = df.columns
    
    # Find closest match
    matches = get_close_matches(name, df_head, n=1, cutoff=similarity_ratio)
    if len(matches) <= 0:
        return None
    else:
        match_index = df_head.index(matches[0])
        return df.columns[match_index]
    
def remove_header_chars(df, chars, case_insensitive=True):  # *
    """Removes chars in string from df header.

    Args:
        df (pandas DataFrame): DataFrame containing header with chars to remove.
        chars (str): Continuous string of chars to individually remove.
        case_insensitive (bool, optional): If True, converts both to lower before comparing. Defaults to True.

    Returns:
        pandas DataFrame: DataFrame with header chars removed.
    """
    df = df.copy()
    
    # Convert both to lowercase
    if case_insensitive:
        chars += chars.upper() + chars.lower()
    
    for column_name in df.columns:
        translate_remove = column_name.maketrans('', '', chars)
        new_column_name = column_name.translate(translate_remove)
        df.rename(columns={column_name: new_column_name}, inplace=True)

    return df

def convert_to_nan(df, na=('', 'nan', 'none')):  # *
    """Converts all instances found in na to np.nan. Case insensitive.

    Args:
        df (pandas DataFrame): Input DataFrame
        na (iterable, optional): Contains patterns to convert. Defaults to ('', 'nan', 'none').

    Returns:
        pandas DataFrame: DataFrame replaced to nan.
    """
    na = [s.lower() for s in na]
    return df.applymap(lambda s: np.nan if str(s).lower() in na else s)

def non_num_to_nan(df, columns):  # *
    """Removes all non numeric (0-9) characters from columns specified.

    Args:
        df (pandas DataFrame): Contains non-numeric values.

    Returns:
        pandas DataFrame: Non-numerics replaced w np.nan.
    """
    
    # Cast to dataframe in case series (1 column)
    try:
        df = df[columns].applymap(lambda s: re.sub('[^0-9]', '', str(s))).replace('', np.nan)
    except AttributeError: 
        df[columns] = df[columns].map(lambda s: re.sub('[^0-9]', '', s)).replace('', np.nan)
        
    return df

def nan_col_indices(df, column_name):  # *
    # replace_blanks_w_na(df)
    return df[df[column_name].isnull()].index.tolist()

def remove_nan_cols(df):  # *
    """Removes columns that are ENTIRELY blank or NaN.

    Args:
        df (pandas DataFrame): DataFrame containing columns to drop.

    Returns:
        pandas DataFrame: DataFrame with columns dropped.
    """
    return convert_to_nan(df).dropna(axis=1, how="all")

def remove_nan_rows(df, value_column_names):  # *
    """Removes entire rows from df where value columns are blank or NaN.

    Args:
        df (pandas DataFrame): DataFrame containing column with NaN values.
        value_column_name (iterable): Contains column names to look for.

    Returns:
        pandas DataFrame: DataFrame with rows dropped where value is NaN.
    """
    return df.dropna(axis=0, subset=value_column_names).reset_index(drop=True)
