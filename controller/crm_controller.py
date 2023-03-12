from model.crm import crm
from model import util
from view import terminal as view

def list_customers():
    data = crm.load_data(1)
    view.print_table(data)


def add_customer():
    data = crm.load_data(1)
    user_data = view.get_inputs(data[0][1:])
    user_id = [util.generate_id()]
    new_user = user_id + user_data
    data.append(new_user)
    crm.save_data(data)
    show_user = list()
    show_user.append(data[0])
    show_user.append(new_user)
    view.print_table(show_user)



def update_customer():
    view.print_error_message("Not implemented yet.")


def delete_customer():
    view.print_error_message("Not implemented yet.")


def get_subscribed_emails():
    users_list = crm.load_data()
    subscribed_emails_list = list()
    for user in users_list:
        user[3] == "1" and subscribed_emails_list.append(user[2])
    view.print_general_results(subscribed_emails_list, "SUBSCRIBED CUSTOMERS EMAILS")

def run_operation(option):
    if option == 1:
        list_customers()
    elif option == 2:
        add_customer()
    elif option == 3:
        update_customer()
    elif option == 4:
        delete_customer()
    elif option == 5:
        get_subscribed_emails()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List customers",
               "Add new customer",
               "Update customer",
               "Remove customer",
               "Subscribed customer emails"]
    view.print_menu("Customer Relationship Management", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
