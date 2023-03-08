from controller import main_controller
from model import data_manager
from controller import crm_controller

def clear_display():
    print("\033c")


# BASIC TESTING FIELD
#a = data_manager.read_table_from_file("model/crm/crm.csv")

#print(crm_controller.list_customers())
#print(crm_controller.add_customer())
#print(crm_controller.get_subscribed_emails())
#print(crm_controller.get_subscribed_emails())
print(crm_controller.get_subscribed_emails())
clear_display()
main_controller.display_menu()
#crm_controller.add_customer()

#if __name__ == '__main__':
#    main_controller.menu()
