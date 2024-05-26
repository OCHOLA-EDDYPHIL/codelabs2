"""
This module has all the reusable functions for tasks
"""
import pandas as pd
import os


def generate_email(full_name):
    # Split the full name into individual names
    names = full_name.split()

    # Extract the first two names
    first_name = names[0] if len(names) >= 1 else ''
    second_name = names[1] if len(names) >= 2 else ''

    # Extract the first letter of the first name
    first_initial = first_name[0] if first_name else ''

    # Combine the first initial, second name, and a domain to form the email
    email = f"{first_initial.lower()}{second_name.lower()}@gmail.com"

    return email


def special_character_names(df, output_path):
    special_char_names = df[df['Student Name'].str.contains("'", na=False)]
    special_char_names.to_csv(os.path.join(output_path, 'special_char_names.csv'), index=False)

    with open(os.path.join(output_path, 'logs.txt'), 'a') as log_file:
        log_file.write(f"Special character names:\n{special_char_names.to_string(index=False)}\n")


def read_excel_file(file_path) -> list:
    df = pd.read_excel(file_path)
    return df.to_dict(orient='records')


def separate_by_gender(df):
    males = df[df['Gender'] == 'M']
    females = df[df['Gender'] == 'F']
    return males, females
