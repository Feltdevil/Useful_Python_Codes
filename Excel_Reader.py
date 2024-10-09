# Before running the code, please ensure you have the required packages installed. You can install them using the following commands:

# pandas: Used for handling Excel files and data manipulation.
# tabulate: Used for formatting the output in a neatly aligned table.

import pandas as pd
from tabulate import tabulate

def extract_data():
    print("What Do You Want To Extract?\nOptions: Whole_File, One_Sheet_Only, Column_Only, Row_Only, Age_Only")
    
    # Asking user for the name of the Excel file
    excel_file = input("Enter the name of the Excel file (without .xls extension): ") + ".xls"
    
    # Asking user for extraction type
    extraction_type = input("Select what you want to extract: Whole_File, One_Sheet_Only, Column_Only, Row_Only, Age_Only: ")
    
    # Load the Excel file
    try:
        df = pd.read_excel(excel_file)
    except FileNotFoundError:
        print(f"File '{excel_file}' not found. Please ensure it is in the same folder.")
        return

    # Whole file extraction
    if extraction_type == 'Whole_File':
        print("\nExtracting the whole file:")
        print(tabulate(df, headers='keys', tablefmt='grid'))
    
    # One sheet extraction
    elif extraction_type == 'One_Sheet_Only':
        sheet_name = input("Enter the sheet name: ")
        try:
            df = pd.read_excel(excel_file, sheet_name=sheet_name)
            print(f"\nExtracting sheet '{sheet_name}':")
            print(tabulate(df.head(), headers='keys', tablefmt='grid'))
        except ValueError:
            print(f"Sheet '{sheet_name}' not found in the file.")
    
    # Column extraction
    elif extraction_type == 'Column_Only':
        column_name = input("Enter the column name: ")
        if column_name in df.columns:
            column_data = df[[column_name]]  # Using double brackets to retain DataFrame format
            print(f"\nExtracting data from column '{column_name}':")
            print(tabulate(column_data, headers='keys', tablefmt='grid'))
        else:
            print(f"Column '{column_name}' not found in the file.")
    
    # Row extraction
    elif extraction_type == 'Row_Only':
        row_index = int(input("Enter the row index: "))
        if 0 <= row_index < len(df):
            row_data = df.iloc[[row_index]]  # Using double brackets to retain DataFrame format
            print(f"\nExtracting data from row {row_index}:")
            print(tabulate(row_data, headers='keys', tablefmt='grid'))
        else:
            print(f"Row index {row_index} is out of range.")
    
   # Age filtering
    elif extraction_type == 'Age_Only':
        if 'Age' in df.columns:
            age_condition = input("Do you want to filter by age? Type 'greater', 'smaller', or 'equal': ").strip().lower()
            age_value = int(input("Enter the age value to filter by: "))
            
            if age_condition == 'greater':
                filtered_df = df[df['Age'] > age_value]
                print(f"\nFiltered rows where 'Age' is greater than {age_value}:")
            elif age_condition == 'smaller':
                filtered_df = df[df['Age'] < age_value]
                print(f"\nFiltered rows where 'Age' is smaller than {age_value}:")
            elif age_condition == 'equal':
                filtered_df = df[df['Age'] == age_value]
                print(f"\nFiltered rows where 'Age' is equal to {age_value}:")
            else:
                print("Invalid option for age filtering.")
                return
            
            print(tabulate(filtered_df, headers='keys', tablefmt='grid'))
        else:
            print("No 'Age' column found in the file.")

# Run the function to extract data
extract_data()
