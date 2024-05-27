"""
This python module is used to run all the functions in the project
"""
import pandas as pd
from tasks import generate_email, special_character_names, read_excel_file, separate_by_gender, log_message, \
    shuffle_and_save
from time import time
from pathlib import Path

INPUT_FILE_PATH = Path('input_data_files/Test files.xlsx')
OUTPUT_FILE_PATH = Path('output_data_files/')


def main():
    # Checks if input file exists
    if not INPUT_FILE_PATH.exists():
        print(f"Input file not found: {INPUT_FILE_PATH}")
        return
    # Create output directory if it doesn't exist
    if not OUTPUT_FILE_PATH.exists():
        OUTPUT_FILE_PATH.mkdir(parents=True)
        print(f"Created output directory: {OUTPUT_FILE_PATH}")

    # Read the Excel file
    data_list = read_excel_file(INPUT_FILE_PATH)
    if not data_list:
        print("No data read from the Excel file.")
        return

    df = pd.DataFrame(data_list)
    log_message(OUTPUT_FILE_PATH,"DataFrame created from Excel file.")

    # Generate email addresses
    df['Email Address'] = df['Student Name'].apply(generate_email)

    # Save the DataFrame with emails to the output directory
    df.to_csv(f"{OUTPUT_FILE_PATH}/output_with_emails.csv", index=False)
    log_message(OUTPUT_FILE_PATH,"Emails generated and saved to CSV file.")
    log_message(OUTPUT_FILE_PATH, f"Generated emails: \n{df[['Student Name', 'Email Address']].to_string(index=False)}")

    # Separate by gender
    separate_by_gender(df, OUTPUT_FILE_PATH)

    # Process special character names and log them
    special_character_names(df, OUTPUT_FILE_PATH)

    # Shuffle and save the data
    shuffle_and_save(df, OUTPUT_FILE_PATH)


if __name__ == '__main__':
    start_time = time()
    main()
    execution_time = time() - start_time
    log_message(OUTPUT_FILE_PATH, f"Execution time: {execution_time}")
    print(f"Execution time: {execution_time} seconds")
