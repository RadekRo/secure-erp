""" Customer Relationship Management (CRM) module

Data table structure:
    - id (string)
    - name (string)
    - email (string)
    - subscribed (int): Is subscribed to the newsletter? 1: yes, 0: no
"""
from model import data_manager, util

DATAFILE = "model/crm/crm.csv"
DATATEMP = "model/crm/temp.csv"
HEADERS = ["id", "name", "email", "subscribed"]

def load_data(header = 0):    
    users_list = data_manager.read_table_from_file(DATAFILE)
    header == 1 and users_list.insert(0, HEADERS)
    return users_list

def save_data(incoming_data):
    data_manager.write_table_to_file(DATATEMP, incoming_data)
