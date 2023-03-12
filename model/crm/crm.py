""" Customer Relationship Management (CRM) module

Data table structure:
    - id (string)
    - name (string)
    - email (string)
    - subscribed (int): Is subscribed to the newsletter? 1: yes, 0: no
"""
from model import data_manager, util

DATAFILE = "model/crm/crm.csv"
HEADERS = ["id", "name", "email", "subscribed"]

def load_data(header = "no-header"):    
    crm_data = data_manager.read_table_from_file(DATAFILE)
    header == "with-header" and crm_data.insert(0, HEADERS)
    return crm_data

def save_data(incoming_data):
    incoming_data.remove(incoming_data[0])
    data_manager.write_table_to_file(DATAFILE, incoming_data)
