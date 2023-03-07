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

def load_data(header = 0):    
    users_list = data_manager.read_table_from_file(DATAFILE)
    if header == 1:
        users_list.insert(0, HEADERS)
    return users_list

def save_data():
    pass
