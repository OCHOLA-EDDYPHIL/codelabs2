"""
This modula has all the reusable functions for tasks
"""
import re
import pandas as pd
import numpy as np


def generate_email(first_name, last_name):
    clean_last_name = re.sub(r'\W+', '', last_name).lower()
    return f"{first_name[0].lower()}{clean_last_name}@gmail.com"


def generate_special_char_names():
    pass


def read_excel_file() -> list:
    pass
