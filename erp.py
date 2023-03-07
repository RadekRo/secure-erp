from controller import main_controller
from model import data_manager
from controller import crm_controller

# BASIC TESTING FIELD
#a = data_manager.read_table_from_file("model/crm/crm.csv")
print(crm_controller.get_subscribed_emails())

#if __name__ == '__main__':
#    main_controller.menu()
