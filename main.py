"""
This python module is used to run all the functions in the project
"""
import pandas as pd
import tasks
from time import time

INPUT_FIlE_PATH = 'input_data_files/'
OUTPUT_FILE_PATH = 'output_data_files/'


if __name__ == '__main__':
    print(time())

def main():
 # Generate email addresses
    df['Email'] = df.apply(lambda row: generate_email(row['First Name'], row['Last Name']), axis=1)


# Shuffle and save
shuffle_and_save(df)

# Save email addresses to CSV and TSV
df.to_csv('students_with_emails.csv', index=False)
df.to_csv('students_with_emails.tsv', sep='\t', index=False)

print("Email addresses generated and files saved.")