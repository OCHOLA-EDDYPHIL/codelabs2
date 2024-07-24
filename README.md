# Project Title

Student Data Manipulation and Analysis - EMAIL GENERATOR

## Description

This project includes a collection of Python scripts designed to manipulate and analyze student data. It provides functionalities such as generating emails based on student names, separating data by gender, handling special characters in names, reading Excel files, and shuffling data for randomization. The project aims to assist in managing and processing student records efficiently.

## Getting Started

### Dependencies

- Python 3.8 or higher
- pandas
- openpyxl (for reading Excel files)

### Installing

1. Clone the repository to your local machine: git clone https://github.com/OCHOLA-EDDYPHIL/codelabs2.git
2. Install the required packages: pip install pandas openpyxl

### Executing Program

1. Navigate to the project directory.
2. Run the script of your choice. For example, to generate emails: python `tasks.py`
3. Replace `tasks.py` with the script you wish to run.

## Features

- **Email Generation**: Generate email addresses based on student names.
- **Special Character Handling**: Identify names with special characters and process them accordingly.
- **Gender Separation**: Separate student records by gender.
- **Excel File Reading**: Read student data from Excel files.
- **Data Shuffling**: Randomize the order of student records.

## Documentation

The `tasks.py` file contains several functions:

- `generate_email(full_name)`: Generates an email address for a given full name.
- `special_character_names(df, output_path)`: Identifies names with special characters and saves them to a CSV file.
- `read_excel_file(file_path)`: Reads student data from an Excel file and returns it as a list of dictionaries.
- `separate_by_gender(df, output_path)`: Separates student records by gender and saves them to separate CSV files.
- `shuffle_and_save(df, output_path)`: Shuffles the student records and saves them in both JSON and JSONL formats.

## Contributing

Contributions are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the [MIT License](LICENSE.md) - see the LICENSE file for details.