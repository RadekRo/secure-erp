from model.crm import crm
from model import util
from view import terminal as view

def find_data(search_value, data):
    for i, row in enumerate(data):
        for j, element in enumerate(row):
            if element == search_value:
                return i
    return False

def get_single_user_data(headers, user_data):
    user = list()
    user.extend([headers, user_data])
    return user

def list_customers():
    database = crm.load_data("with-header")
    view.print_table(database)

def add_customer():
    database = crm.load_data("with-header")
    user_data = view.get_inputs(database[0][1:])
    user_id = [util.generate_id()]
    new_user = user_id + user_data
    show_added_user = get_single_user_data(database[0], new_user)
    database.append(new_user)
    crm.save_data(database)
    view.print_table(show_added_user)

def update_customer():
    database = crm.load_data("with-header")
    user_id = view.get_input("Enter user id to edit")
    find_user = find_data(user_id, database)
    if find_user != False:
        user_data = view.get_inputs(database[0][1:])
        database[find_user][1::] = user_data
        crm.save_data(database) 
        view.print_message(f"User of id: {user_id} has been updated.")
    else:
        view.print_error_message("No user found with provided id.")

def delete_customer():
    database = crm.load_data("with-header")
    user_id = view.get_input("Enter user id to delete")
    find_user = find_data(user_id, database)
    if find_user != False:
        view.print_message(f"User id: {user_id} deleted from the database.")
        database.remove(database[find_user])
        crm.save_data(database) 
    else:
        view.print_error_message("No user found with provided id.")

def get_subscribed_emails():
    database = crm.load_data()
    subscribed_emails_list = list()
    for user in database:
        user[3] == "1" and subscribed_emails_list.append(user[2])
    if len(subscribed_emails_list) > 0:
        view.print_general_results(subscribed_emails_list, "SUBSCRIBED CUSTOMERS EMAILS")
    else:
        view.print_error_message("USERS WITH ACTIVE SUBSCRIPTION NOT FOUND!")

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
