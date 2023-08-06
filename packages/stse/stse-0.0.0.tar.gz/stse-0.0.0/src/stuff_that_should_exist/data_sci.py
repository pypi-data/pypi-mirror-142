# import numpy as np
# import pandas as pd
# import warnings


# def bit_vect(length, indices):
#     """Generates a bit vector, hot at each index and 0 everywhere else.

#     Args:
#         length (int): Length of desired bit vector.
#         length
#         indices (iter(int)): List of indices to equal 1.

#     Returns:
#         np.array: bit vector.
#     """
#     out = np.zeros(length)
#     out[indices] = 1
#     return out

# def read_spreadsheet(file, return_ext=False):

#     # Get file MIME
#     file_mime = file.content_type

#     # Read CSV
#     if file_mime == 'text/csv':
#         file_ext = 'csv'

#         # Read in data
#         input_data = pd.read_csv(file)
        
#     # Read TSV
#     elif file_mime == 'text/tab-separated-values':
#         file_ext = 'tsv'

#         # Read in data
#         input_data = pd.read_csv(file, sep='\t')
        
#     # Read Excel
#     elif (file_mime == 'application/vnd.ms-excel' or
#           file_mime == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'):
#         file_ext = 'xlsx'

#         # Read in data
#         input_data = pd.read_excel(file)

#     # Unsupported filetype
#     else:
#         warnings.warn(f'"{file_mime}" is not a supported filetype.')


#     return input_data, file_ext if return_ext else input_data

# def drop_val(df, col_name, value):  # *
#     """Drops row from df where column entry is equal to value.

#     Args:
#         df (pandas DataFrame): DataFrame containing rows to drop.
#         col_name (str): Name of column to investigate.
#         value (pandas object): Value to drop instances of.

#     Returns:
#         pandas DataFrame: DataFrame with rows dropped.
#     """
#     return pull_not_val(df, col_name, value).reset_index(drop=True)

# def pull_val(df, col_name, value):  # *
#     """Retrieves rows from df where column entry is equal to value.

#     Args:
#         df (pandas DataFrame): DataFrame containing rows to pull.
#         col_name (str): Name of column to investigate.
#         value (pandas object): Value to pull instances of.

#     Returns:
#         pandas DataFrame: DataFrame where value is found.
#     """
#     return df.where(df[col_name] == value).dropna()

# def pull_not_val(df, col_name, value):  # *
#     """Retrieves rows from df where column entry is not equal to value.

#     Args:
#         df (pandas DataFrame): DataFrame containing rows to pull.
#         col_name (str): Name of column to investigate.
#         value (pandas object): Value to not pull instances of.

#     Returns:
#         pandas DataFrame: DataFrame where value is not found.
#     """
#     return df.where(df[col_name] != value).dropna()

# def filter_duplicates(df, subsets, return_duplicates=False, how='all'):  # *
#     """Filters duplicates to either return DataFrame subset of duplicates or non-duplicates.

#     Args:
#         df (pandas DataFrame): DataFrame to perform duplicate search on.
#         subsets (list): List of column names to compare in duplicate search.
#                         All must match to be considered a duplicate.
#         return_duplicates (bool, optional): If True, returns non-duplicate df else returns duplicate df.
#                                             Defaults to False.
#         how (str): 

#     Returns:
#         pandas DataFrame: Filtered df.
#     """
#     if how == 'any' and len(subsets) > 1:
#         # Checks for occurances in ANY column of 'subsets'
#         index_arr = np.array([])
#         for col in subsets:     
#             index_arr = np.concatenate((index_arr, indices(df, col)))
        
#         index_arr = np.unique(index_arr)
        
#         return df.loc[df.index.isin(index_arr)] if return_duplicates else df.loc[~df.index.isin(index_arr)]
    
#     elif how == 'all':
#         # Duplicates in ALL columns of 'subsets' must agree
#         duplicates = pd.DataFrame.duplicated(df, subset=subsets)
        
#     else:
#         # Raise error of how is not 'any' or 'all'
#         raise ValueError('how argument must be either \'any\' or \'all\'')
    
#     return df[duplicates] if return_duplicates else df[~duplicates]

# def remove_duplicates(df, subsets):  # *
#     """Removes duplicates from df. Keeps first occurance in df.

#     Args:
#         df (pandas DataFrame): DataFrame to perform dupicate search on.
#         subsets (list): List of column names to compare in duplicate search.
#                         All must match to be considered a duplicate.

#     Returns:
#         pandas DataFrame: DataFrame with duplicates removed.
#     """
#     return filter(df, subsets=subsets)