import pandas as pd

df_first = pd.read_excel('Table/1.xlsx')
df_second = pd.read_excel('Table/2.xlsx')
df_third = pd.read_excel('Table/3.xlsx') 

table1 = df_first
table2 = df_second

df_first.index = range(df_first.iloc[0]['id'], df_first['id'].iloc[-1] + 1, 1)
df_first.index.name = 'id'

count = df_second['id'].count()
