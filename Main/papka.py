import pandas as pd
import openpyxl

df_first = pd.read_excel('Main/1.xlsx')
df_second = pd.read_excel('Main/2.xlsx')
df_third = pd.read_excel('Main/3.xlsx') 

table1 = df_first
table2 = df_second

df_first.index = range(df_first.iloc[0]['id'], df_first['id'].iloc[-1] + 1, 1)
df_first.index.name = 'id'

count = df_second['id'].count()

df_second.index = range(df_first['id'].iloc[-1] + 1, df_first['id'].iloc[-1] + 1 + count, 1)
df_second.index.name = 'id'

count_2 = df_third['id'].count()

df_third.index = range(df_second['id'].iloc[-1] + 1, df_second['id'].iloc[-1] + 1 + count_2, 1)
df_third.index.name = 'id'

df_first.to_csv('new_table1.exel', index=False)
df_second.to_csv('new_table2.exel', index=False)
df_third.to_csv('new_table3.exel', index=False)