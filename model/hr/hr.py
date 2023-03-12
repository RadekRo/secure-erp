""" Human resources (HR) module

Data table structure:
    - id (string)
    - name (string)
    - birth date (string): in ISO 8601 format (like 1989-03-21)
    - department (string)
    - clearance level (int): from 0 (lowest) to 7 (highest)
"""

from model import data_manager, util

DATAFILE = "model/hr/hr.csv"
HEADERS = ["Id", "Name", "Date of birth", "Department", "Clearance"]

def load_data(header = "no-header"):    
    hr_data = data_manager.read_table_from_file(DATAFILE)
    header == "with-header" and hr_data.insert(0, HEADERS)
    return hr_data

def save_data(incoming_data):
    incoming_data.remove(incoming_data[0])
    data_manager.write_table_to_file(DATAFILE, incoming_data)