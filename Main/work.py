import pandas as pd
import openpyxl

def merge_excel_files(file_paths, output_folder_path):
    last_id = 0
    legth_check = 0
    for i, file_path in enumerate(file_paths):
        df = pd.read_excel('Table/' + file_path)
        if i == 0:
            last_id = df.iloc[0]['id']
        else:    
            last_id += length_check
        df['id'] = range(last_id + 1,last_id + len(df) + 1)
        output_file_path = f'{output_folder_path}/new_table{i+1}.csv'
        df.to_csv(output_file_path, index=False)
        length_check = len(df)

file_paths = ['1.xlsx', '2.xlsx', '3.xlsx']
output_folder_path = 'Table'
merge_excel_files(file_paths, output_folder_path)