import pandas as pd

# List of customers and products
customers = pd.read_csv('master_data/customers.csv')
customers = list(customers['ID'])
products = pd.read_csv('master_data/products.csv')
products = list(products['ID'])
users = pd.read_csv('master_data/users.csv')
users = list(users['Last, First'])

# Strategy
Strategy = list([
'strategy1',
'strategy2',
'strategy3'
])

# Others
Type = list(['typ1','typ2'])
Payment_Frequency = list(['Monthly','Quarterly','Semi-annually','Annually'])
Level = list(['lvl1','lvl2'])
Payment_Method = list(['method1', 'method2'])
SubType = list(['type1','type2', 'typ3'])
Program_Name = list(['name1', 'name2', 'name3'])
Lines_From = list(['line1', 'line2', 'line3'])
Schedule_Basis = list(['s1', 's2', 's3'])
Rebate_Product_Inclusion = list(['Product', 'Program'])
Baseline = list(['bs1', 'bs2', 'bs3'])
Growth_Type = list(['Growth','Percentage'])