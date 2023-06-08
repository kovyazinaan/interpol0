from work import merge_excel_files
import pandas as pd
import openpyxl
if __name__ == "__main__":
    file_paths = ['1.xlsx', '2.xlsx', '3.xlsx']
    output_folder_path = 'Main'
    merge_excel_files(file_paths, output_folder_path)
