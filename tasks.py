"""
This module has all the reusable functions for tasks
"""
import pandas as pd
import os


def generate_email(name):
    clean_name = ''.join(e for e in name if e.isalnum()).lower()
    return f"{clean_name}@gmail.com"


def special_character_names(df, output_path):
    # Assuming "student names" column contains all names
    special_char_names = df[df['Student Name'].str.contains(r'[^\w\s]', na=False)]
    special_char_names.to_csv(os.path.join(output_path, 'special_char_names.csv'), index=False)

    with open(os.path.join(output_path, 'logs.txt'), 'a') as log_file:
        log_file.write(f"Special character names:\n{special_char_names.to_string(index=False)}\n")


def read_excel_file(file_path) -> list:
    df = pd.read_excel(file_path)
    return df.to_dict(orient='records')
