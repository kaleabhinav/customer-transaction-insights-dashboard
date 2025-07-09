import pandas as pd


def read_data(path):
    """
    This function takes a csv path and read it using pandas read_csv function
    Returns a pandas dataframe
    """
    df = pd.read_csv(path)

    return df

def how_many_customers(df,col_name):

    """
    This function is to print how many customers are present in the csv file
    I/P : Pandas dataframe and a column name
    O/P : Number of unique values present in that column
    """

    return df[col_name].nunique()

def get_max_value(df,col_name):

    max_value = df[col_name].max()

    return max_value

def get_filtered_row(df,col_name):

    return df[df[col_name] == get_max_value(df = df,col_name = col_name)]