"""
This python module is used to run all the functions in the project
"""
import os

import pandas as pd
from tasks import generate_email, special_character_names, read_excel_file
from time import time

INPUT_FILE_PATH = 'input_data_files/Test files.xlsx'
OUTPUT_FILE_PATH = 'output_data_files/'


def main():
    if not os.path.exists(INPUT_FILE_PATH):
        print(f"Input file not found: {INPUT_FILE_PATH}")
        return

    if not os.path.exists(OUTPUT_FILE_PATH):
        os.makedirs(OUTPUT_FILE_PATH)
        print(f"Created output directory: {OUTPUT_FILE_PATH}")

    # Read the Excel file
    data_list = read_excel_file(INPUT_FILE_PATH)
    if not data_list:
        print("No data read from the Excel file.")
        return

    df = pd.DataFrame(data_list)
    print("DataFrame created.")

    # Generate email addresses
    df['Email'] = df['Student Name'].apply(generate_email)
    print("Emails generated.")

    # Save the DataFrame with emails to the output directory
    output_csv_path = os.path.join(OUTPUT_FILE_PATH, 'output_with_emails.csv')
    df.to_csv(output_csv_path, index=False)
    print(f"Output saved to {output_csv_path}")

    # Process special character names and log them
    special_character_names(df, OUTPUT_FILE_PATH)
    print(f"Special character names and logs saved to {OUTPUT_FILE_PATH}")


if __name__ == '__main__':
    start_time = time()
    main()
    print(f"Execution time: {time() - start_time} seconds")
