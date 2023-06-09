import pandas as pd

# List of customers and products
customers = pd.read_csv('master_data/customers.csv')
customers = list(customers['ID'])
products = pd.read_csv('master_data/products.csv')
products = list(products['ID'])
users = pd.read_csv('master_data/users.csv')
users = list(users['Last, First'])

# Rebate Strategy
Rebate_Strategy = list([
'BSC_MS by Rev - Amt per Unit',
'BSC_MS by Rev - Fixed Amt',
'BSC_MS by Rev - Percent off Invoice',
'BSC_MS by Vol - Amt per Unit',
'BSC_MS by Vol - Fixed Amt' ,
'BSC_MS by Vol - Percent off Invoice', 
'BSC_MS by Vol - Percent off over Growth Sales',
'BSC_Revenue - Amt per Unit' ,
'BSC_Revenue - Percent off Invoice', 
'BSC_Revenue - Fixed Amt' ,
'BSC_Revenue - Step Tiered',
'BSC_Rev - Per off Inv (Capped)',
'BSC_Revenue - Net Price',
'BSC_Revenue - Percent off over Growth Sales',
'BSC_Volume - Amt per Unit' ,
'BSC_Volume - Percent off Invoice' ,
'BSC_Volume - Percent off over Growth Sales',
'BSC_Volume - Fixed Amt',
'BSC_Volume - Capped Amt per Unit',
'BSC_Volume - AmtPerUnit (Tracker - Emory)',
'BSC_Amt per Unit (Tracker CCO)_New',
'BSC_Capitated Rebate (Tracker)',
'BSC_Non Standard',
'BSC_Percent off Invoice (Tracker CCO)_New',
'BSC_Revenue - AmtPerUnit(Tracker - Excelerate)',
'BSC_Growth in Rev over Baseline - Amt per Unit',
'BSC_Growth in Rev over Baseline - Fixed Amt',
'BSC_Growth in Rev over Baseline - Percent off Invoice',
'BSC_Growth in Vol over Baseline - Amt per Unit',
'BSC_Growth in Vol over Baseline - Fixed Amt',
'BSC_Growth in Vol over Baseline - Percent off Invoice',
'BSC_Volume - AmtPerUnit (Tracker - Emory)',
  
# sceond time
'BSC_MS by Rev - Amt per Unit',
'BSC_MS by Rev - Fixed Amt',
'BSC_MS by Rev - Percent off Invoice',
'BSC_MS by Vol - Amt per Unit',
'BSC_MS by Vol - Fixed Amt' ,
'BSC_MS by Vol - Percent off Invoice', 
'BSC_MS by Vol - Percent off over Growth Sales',
'BSC_Revenue - Amt per Unit' ,
'BSC_Revenue - Percent off Invoice', 
'BSC_Revenue - Fixed Amt' ,
'BSC_Revenue - Step Tiered',
'BSC_Rev - Per off Inv (Capped)',
'BSC_Revenue - Net Price',
'BSC_Revenue - Percent off over Growth Sales',
'BSC_Volume - Amt per Unit' ,
'BSC_Volume - Percent off Invoice' ,
'BSC_Volume - Percent off over Growth Sales',
'BSC_Volume - Fixed Amt',
'BSC_Volume - Capped Amt per Unit',
'BSC_Volume - AmtPerUnit (Tracker - Emory)',
'BSC_Amt per Unit (Tracker CCO)_New',
'BSC_Capitated Rebate (Tracker)',
'BSC_Non Standard',
'BSC_Percent off Invoice (Tracker CCO)_New',
'BSC_Revenue - AmtPerUnit(Tracker - Excelerate)',
'BSC_Growth in Rev over Baseline - Amt per Unit',
'BSC_Growth in Rev over Baseline - Fixed Amt',
'BSC_Growth in Rev over Baseline - Percent off Invoice',
'BSC_Growth in Vol over Baseline - Amt per Unit',
'BSC_Growth in Vol over Baseline - Fixed Amt',
'BSC_Growth in Vol over Baseline - Percent off Invoice',
'BSC_Volume - AmtPerUnit (Tracker - Emory)'])

# Others
Accrual_Type = list(['%','Amount / unit'])
Payment_Frequency = list(['Monthly','Quarterly','Semi-annually','Annually'])
Payment_Level = list(['Aggregate','Member'])
Payment_Method = list(['ACH','Check','CM - Open Invoice','Credit Memo','Customer Defined','Purchase Credit','Wired'])
Rebate_SubType = list(['Capital Equipment','CrossCare ADV','CrossCare CRV','CrossCare CV','CrossCare ES','Net Price Rebate',
'Non-Standard','Standard - Admin Fee','Standard - Rebate'])
Program_Name = list(['SALES_SCS+VF+RF','UNITS_SCS','UNITS_VF','SALES_SCS+VF+RF+DBS','UNITS_DBS'])
Calculation_Level = list(['Sold-to','Product','Product, Sold-to'])
Transaction_Lines_From = list(["All Transactions","This contract only","This and other Non-group Contracts",
"Included Contracts", "All but excluded Contracts","Included Program"])
Schedule_Basis = list(["Commitment based","Calendar based","Alternate Calendar based","Program based","Reference to Start of Month"])
Accrue_In_ERP = list(['TRUE','FALSE'])
Rebate_Product_Inclusion = list(['Product', 'Program'])
Baseline = list(['2 Periods Prior','3 Periods Prior','4 Periods Prior','Manually Set Value','Prior Period'])
Growth_Type = list(['Growth = (Current/Baseline -1)*100%','Percentage = (Current/Baseline)*100%','Delta = Current-Baseline'])