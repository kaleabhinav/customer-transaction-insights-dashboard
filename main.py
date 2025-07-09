from config import DirConfig
from utils import *

# Initializing config
DIR_CONFIG = DirConfig()

# Reading the data
df = read_data(DIR_CONFIG.data_path)

# print(df.shape)

print(f"Number of rows in the file : {df.shape[0]}")

print(f"Number of customers present in the file : {how_many_customers(df = df ,col_name='CUST_ID')}")


get_filtered_row()
