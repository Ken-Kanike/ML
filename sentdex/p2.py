import pandas as pd

# Load the Excel file
df = pd.read_excel("yahoo_data.xlsx")  

# Print first 5 rows
# print(df.head())
# df => data frame

#df = df[['Open', 'Close*', 'Low', 'High']]  # selecting only requeired cols

# do data operations and calculations 
df['HL_PCT'] = (df['High'] - df['Low']) / df['Close*'] * 100.0
df['PCT_change'] = (df['Close*'] - df['Open']) / df['Open'] * 100.0

df = df[['Close*', 'HL_PCT', 'PCT_change','Open']]
print(df.head())