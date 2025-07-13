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

def which_customer_spends_most(df):
    max_spend = df['PURCHASES'].max()
    cust_id = df[df['PURCHASES'] == max_spend]['CUST_ID'].iloc[0]
    return [max_spend, cust_id]

def get_less_risk_customers(df):

    df['CREDIT_UTILIZATION'] = df['BALANCE']/df['CREDIT_LIMIT']

    df_credit_limit = df[df['CREDIT_UTILIZATION'] <= 0.4] 

    df_final = df_credit_limit[df_credit_limit['PRC_FULL_PAYMENT'] == 1]

    cust_list = list(df_final.CUST_ID.unique())

    return cust_list

def get_risky_customers(df):

    df['CREDIT_UTILIZATION'] = df['BALANCE']/df['CREDIT_LIMIT']

    df_credit_limit = df[df['CREDIT_UTILIZATION'] > 0.4] 

    df_final = df_credit_limit[df_credit_limit['PRC_FULL_PAYMENT'] != 1]

    cust_list = list(df_final.CUST_ID.unique())

    return cust_list

def get_loyal_customers(df):

    df_tenure = df[df['TENURE'] > 6]

    df_final = df_tenure[df_tenure['PRC_FULL_PAYMENT'] > 0.9]
    
    cust_list = list(df_final.CUST_ID.unique())

    return cust_list