""" Sales module

Data table structure:
    - id (string)
    - customer id (string)
    - product (string)
    - price (float)
    - transaction date (string): in ISO 8601 format (like 1989-03-21)
"""

from model import data_manager, util

DATAFILE = "model/sales/sales.csv"
HEADERS = ["Id", "Customer", "Product", "Price", "Date"]

def load_data(header = 0):    
    transaction_list = data_manager.read_table_from_file(DATAFILE)
    header == 1 and transaction_list.insert(0, HEADERS)
    return transaction_list

def save_data(incoming_data):
    incoming_data.remove(incoming_data[0])
    data_manager.write_table_to_file(DATAFILE, incoming_data)