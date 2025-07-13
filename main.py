from config import DirConfig
from utils import *

# Initializing config
DIR_CONFIG = DirConfig()

# Reading the data
df = read_data(DIR_CONFIG.data_path)

print(f"Number of rows in the file : {df.shape[0]}")
print('\n')

print(f"Number of customers present in the file : {how_many_customers(df = df ,col_name='CUST_ID')}")


print('\n')
print("WHO SPENDS THE MOST")
print('\n')

# 1. Which customer does the most spend?

print(f"""The customer who spends the most : {which_customer_spends_most(df=df)[1]},the amount of spend : {which_customer_spends_most(df=df)[0]}""")

# 2. Who are less risk customers? 
print('\n')
print("LESS RISKY CUSTOMERS")
print('\n')
"""
What defines a less risk customer: 
- customers who has used upto 40% of the credit limit
- customers who have returned 100% of the bill [Banks needs to be strict :)]
"""

print(f"Number of less risky customers : {len(get_less_risk_customers(df))}")
print('\n')

print(f"List of less risky customers : {get_less_risk_customers(df)}")

# Who are the risky customers?
print('\n')
print("RISKY CUSTOMERS")
print('\n')
"""
What defines a risky customer: 
- customers who has used beyond 40% of the credit limit
- customers who have not returned 100% of the bill [Banks needs to be strict :)]
"""

print(f"Number of risky customers : {len(get_risky_customers(df))}")
print('\n')

print(f"List of risky customers : {get_risky_customers(df)}")

# Loyal Customers

print('\n')
print("CUSTOMER LOYALTY")
print('\n')

"""
What defines a loyal customers:

Tenure should be more that 6 years
And full payment percentage should be above 90%
"""

print(f"Number of Loyal Customers : {len(get_loyal_customers(df))}")
print('\n')

print(f"List of Loyal Customers : {get_loyal_customers(df)}")
