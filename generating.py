import pandas as pd
import numpy as np
import random
import datetime
import lovs as lovs 
import functions as fun

# Contracct Header and Program
df= pd.read_excel('2023-04-17-NMD_Contract_Conversion_Template_v0.4.xlsx', sheet_name='Rebate Prog (2)')
ch= pd.read_excel('2023-04-17-NMD_Contract_Conversion_Template_v0.4.xlsx', header=2, sheet_name='Contract Header')

# contract names
contract_names = list(ch['Contract Name'][1:])

# empty dataframes
df = df.head(0)
ch = ch.head(0)

### Rebate Program 
# Strategy
df['Rebate Strategy'] = lovs.Rebate_Strategy 

# Dates
start_start_date = pd.to_datetime('01/01/2022')
end_start_date = pd.to_datetime('04/01/2023')
start_end_date = pd.to_datetime('04/30/2023')
end_end_date = end_start = pd.to_datetime('12/30/2026')
df['Program Start Date'] = fun.random_dates(start_start_date, end_start_date, len(df))
df['Program Start Date'] = pd.to_datetime(df['Program Start Date']).dt.strftime('%Y-%m-%d')
df['Program Start Date'] = pd.to_datetime(df['Program Start Date']).dt.strftime('%Y-%m-%d %H:%M')
df['Program End Date'] = fun.random_dates(start_end_date, end_end_date, len(df))
df['Program End Date'] = pd.to_datetime(df['Program End Date']).dt.strftime('%Y-%m-%d')
df['Program End Date'] = pd.to_datetime(df['Program End Date']).dt.strftime('%Y-%m-%d %H:%M')

# Random
df['Customer Contract ID'] = np.random.randint(30000, 60000, len(df)).astype(str)
df['Customer Contract ID'] = '000' + df['Customer Contract ID'].astype(str)
df['# of Tiers'] = np.random.randint(1, 5, len(df))
df['Tier'] = np.random.randint(1, 5, len(df))
df['Tier Basis'] = np.random.randint(1, 1500000, len(df))
df['Tier Benefit'] = np.random.uniform(0.01, 50000, len(df)).round(2)
df['Accrual Rate'] = np.random.uniform(0.01, 5000, len(df)).round(2)
df['Process Date Lag'] = np.random.randint(20, 31, len(df))
df['Late Date Lag'] = np.random.randint(35, 46, len(df))
df['Manual Baseline Value'] = np.random.randint(1000, 5000, len(df))
# Constant
df['Ad. Fee Netting Rule'] = ''

# From lovs
df['Rebated Customer'] = np.random.choice(lovs.customers, len(df))
df['Program Name']= np.random.choice(lovs.Program_Name, len(df))
df['Rebate SubType'] = np.random.choice(lovs.Rebate_SubType, len(df))
df['Calculation Level'] = np.random.choice(lovs.Calculation_Level, len(df))
df['Payment Frequency']= np.random.choice(lovs.Payment_Frequency, len(df))
df['Payment Level']= np.random.choice(lovs.Payment_Level, len(df))
df['Transaction Lines From'] = np.random.choice(lovs.Transaction_Lines_From, len(df))
df['Schedule Basis'] = np.random.choice(lovs.Schedule_Basis, len(df))
df['Payment Method'] = np.random.choice(lovs.Payment_Method, len(df))
df['Accrual Type'] = np.random.choice(lovs.Accrual_Type, len(df))
df['Rebate Product Inclusion'] = np.random.choice(lovs.Rebate_Product_Inclusion, len(df))
df['Accrue In ERP?'] = np.random.choice(lovs.Accrue_In_ERP, len(df))
df['Baseline'] = np.random.choice(lovs.Baseline, len(df))
df['Growth Type'] = np.random.choice(lovs.Growth_Type, len(df))

# based on condition: Accural Rate
for index in df.index:
    if df['Accrual Type'][index] == '%':
        df['Accrual Rate'][index] = np.random.uniform(0.01, 5, 1).round(2)
    else:
        df['Accrual Rate'][index] = np.random.randint(100, 5000, 1).round(2)

# Adding products
for index in df.index:
    df['Products'][index] = np.random.choice(lovs.products, np.random.randint(1, 4))

# splitting products into rows
df = df.explode('Products')
df = df.reset_index(drop = True)

# order of columns
df = df[['Customer Contract ID', 'Program Name', 'Rebate SubType',
       'Program Start Date', 'Program End Date', 'Calculation Level',
       '# of Tiers', 'Payment Frequency', 'Payment Level',
       'Transaction Lines From', 'Schedule Basis', 'Rebate Strategy', 'Tier',
       'Tier Basis', 'Tier Benefit', 'Payment Method', 'Process Date Lag',
       'Late Date Lag', 'Rebated Customer', 'Accrual Type', 'Accrual Rate',
       'Accrue In ERP?', 'Ad. Fee Netting Rule', 'Rebate Product Inclusion',
       'Products','Programs', 'Included Contracts', 'Excluded contracts',
       'Basis 1 Products', 'Basis 1 Programs', 'Basis 1 Included Contracts',
       'Basis 1 Excluded Contracts', 'Basis 2 Products', 'Basis 2 Programs',
       'Basis 2 Included Contracts', 'Basis 2 Excluded Contracts',
       'Baseline','Manual Baseline Value', 'Growth Type'
       ]]

### Contract Header
CtrtSubType = list(['Sold-to-Standard','IDN', ])
ch['Alternate Contract ID'] = df['Customer Contract ID']
ch['Customer Contract ID'] = df['Customer Contract ID']
ch['Customer ID'] = df['Rebated Customer']
ch['Contract Start Date'] = df['Program Start Date']
ch['Contract End Date'] = df['Program End Date']
ch['Contract Domain'] = 'Commercial'
ch['Additional Delegate'] = ''
ch['Contract Type'] = 'Purchase Based'
ch['Evergreen Contract?'] = 'FALSE'
ch['Organization'] = 'Neuromodulation'
ch['Contract Name'] = np.random.choice(contract_names, len(ch))
ch['Contract Sub-type'] = np.random.choice(CtrtSubType, len(ch))
ch['Contract Category'] = np.random.choice(['Non Signing Price Letter', ''], len(ch))
ch['Rebate Program Only?'] = np.random.choice(['TRUE', 'FALSE'], len(ch))
ch['Contract Author'] = np.random.choice(lovs.users, len(ch))
ch['Sales Rep.'] = np.random.choice(lovs.users, len(ch))

# saving as csv
df.to_csv("output/Rebate Program.csv", index = False)
ch.to_csv("output/Contract Header.csv", index = False)