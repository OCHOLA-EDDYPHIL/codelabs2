"""
This module has all the reusable functions for tasks
"""
from datetime import datetime
from pathlib import Path
import pandas as pd
import json


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
    special_char_names.to_csv(f"{output_path}/special_char_names.csv", index=False)
    log_message(output_path, "Special characters generated and saved to CSV file.")
    log_message(output_path, f"Special character names:\n{special_char_names.to_string(index=False)}")


def read_excel_file(file_path) -> list:
    df = pd.read_excel(file_path)
    return df.to_dict(orient='records')


def separate_by_gender(df, output_path):
    males = df[df['Gender'] == 'M']
    females = df[df['Gender'] == 'F']

    males.to_csv(f"{output_path}/males_with_emails.csv", index=False)
    log_message(output_path, f"Number of Males: {len(males)}")
    log_message(output_path, f"Males: \n{males.to_string(index=False)}")

    females.to_csv(f"{output_path}/females_with_emails.csv", index=False)
    log_message(output_path, f"Number of females: {len(females)}")
    log_message(output_path, f"Females: \n{females.to_string(index=False)}")


def log_message(output_path, message):
    log_file_path = f"{output_path}/logs.txt"
    timestamp = datetime.now().strftime("%Y_%m_%d %H:%M:%S")
    with open(log_file_path, 'a') as log_file:
        log_file.write(f"{timestamp}- {message}\n")


def shuffle_and_save(df, output_path):
    # Shuffle DataFrame
    df_shuffled = df.sample(frac=1).reset_index(drop=True)

    # Convert Timestamp objects to strings
    df_shuffled['DoB'] = df_shuffled['DoB'].astype(str)

    # Save as JSON
    df_shuffled.to_json(Path(output_path) / 'shuffled_data.json', orient='records', indent=4)
    log_message(output_path, "Shuffled data saved to JSON.")

    # Save as JSONL
    jsonl_path = Path(output_path) / 'shuffled_data.jsonl'
    with open(jsonl_path, 'w') as jsonl_file:
        for index, row in df_shuffled.iterrows():
            jsonl_entry = {
                "id": str(index),
                "Student_number": row['Student Number'],
                "additional_details": [
                    {
                        "dob": row['DoB'],
                        "gender": row['Gender'],
                        "special_character": "['yes']" if any(
                            char in row['Student Name'] for char in "'") else "['no']"
                    }
                ]
            }
            jsonl_file.write(json.dumps(jsonl_entry) + '\n')
    log_message(output_path, "Shuffled data saved to JSONL.")
