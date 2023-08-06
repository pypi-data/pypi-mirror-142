import pandas as pd
import warnings


class Dataframes:
    def read_spreadsheet(self, file, return_ext=False):

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

    def drop_val(self, df, col_name, value):  # *
        """Drops row from df where column entry is equal to value.

        Args:
            df (pandas DataFrame): DataFrame containing rows to drop.
            col_name (str): Name of column to investigate.
            value (pandas object): Value to drop instances of.

        Returns:
            pandas DataFrame: DataFrame with rows dropped.
        """
        return self.pull_not_val(df, col_name, value).reset_index(drop=True)

    def pull_val(self, df, col_name, value):  # *
        """Retrieves rows from df where column entry is equal to value.

        Args:
            df (pandas DataFrame): DataFrame containing rows to pull.
            col_name (str): Name of column to investigate.
            value (pandas object): Value to pull instances of.

        Returns:
            pandas DataFrame: DataFrame where value is found.
        """
        return df.where(df[col_name] == value).dropna()

    def pull_not_val(self, df, col_name, value):  # *
        """Retrieves rows from df where column entry is not equal to value.

        Args:
            df (pandas DataFrame): DataFrame containing rows to pull.
            col_name (str): Name of column to investigate.
            value (pandas object): Value to not pull instances of.

        Returns:
            pandas DataFrame: DataFrame where value is not found.
        """
        return df.where(df[col_name] != value).dropna()