from model.crm import crm
from view import terminal as view

def list_customers():
    data = crm.load_data()
    for line in data:
        line.pop()
    enum = enumerate(data)
    dictTable = dict((i, j) for i, j in enum)
    view.print_table(dictTable)


def add_customer():
    view.print_error_message("Not implemented yet.")


def update_customer():
    view.print_error_message("Not implemented yet.")


def delete_customer():
    view.print_error_message("Not implemented yet.")


def get_subscribed_emails():
    users_list = crm.load_data()
    subscribed_emails_list = list()
    for user in users_list:
        user[3] == "1" and subscribed_emails_list.append(user[2])
    view.print_general_results(subscribed_emails_list, "Subscribed customers emails")

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
