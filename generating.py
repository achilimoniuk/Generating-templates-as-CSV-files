import pandas as pd
import numpy as np
import random
import datetime
import lovs as lovs 
import functions as fun

# Contracct Header and Program
df= pd.read_excel('file.xlsx', sheet_name='sheet')
ch= pd.read_excel('file1.xlsx', header=2, sheet_name='sheet1')

# Contract names
contract_names = list(ch['Contract Name'][1:])

# Creating empty dataframe from existing file
df = df.head(0)

### Program 
# Strategy
df['Strategy'] = lovs.Strategy 

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

# Random attributes
df['Customer Contract ID'] = np.random.randint(30000, 60000, len(df)).astype(str)
df['Customer Contract ID'] = '000' + df['Customer Contract ID'].astype(str)
df['number1'] = np.random.randint(1, 5, len(df))
df['number2'] = np.random.randint(1, 5, len(df))
df['number3'] = np.random.randint(1, 1500000, len(df))
df['number4'] = np.random.uniform(0.01, 50000, len(df)).round(2)
df['number5'] = np.random.uniform(0.01, 5000, len(df)).round(2)
df['Date Lag'] = np.random.randint(20, 31, len(df))


# Attributes from lovs
df['Type'] = np.random.choice(lovs.Type, len(df))
df['Customer'] = np.random.choice(lovs.customers, len(df))
df['Program Name']= np.random.choice(lovs.Program_Name, len(df))
df['SubType'] = np.random.choice(lovs.SubType, len(df))
df['Level'] = np.random.choice(lovs.Level, len(df))
df['Payment Frequency']= np.random.choice(lovs.Payment_Frequency, len(df))
df['Lines From'] = np.random.choice(lovs.Transaction_Lines_From, len(df))
df['Schedule Basis'] = np.random.choice(lovs.Schedule_Basis, len(df))
df['Payment Method'] = np.random.choice(lovs.Payment_Method, len(df))
df['Baseline'] = np.random.choice(lovs.Baseline, len(df))
df['Growth Type'] = np.random.choice(lovs.Growth_Type, len(df))

# Attributes based on condition: Type
for index in df.index:
    if df['Type'][index] == 'type1':
        df['Rate'][index] = np.random.uniform(0.01, 5, 1).round(2)
    else:
        df['Rate'][index] = np.random.randint(100, 5000, 1).round(2)

# Adding products
for index in df.index:
    df['Products'][index] = np.random.choice(lovs.products, np.random.randint(1, 4))

# Splitting products into rows
df = df.explode('Products')
df = df.reset_index(drop = True)

# saving as csv
df.to_csv("output/Program.csv", index = False)
