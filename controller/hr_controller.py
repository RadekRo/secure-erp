from model.hr import hr
from model import util
from view import terminal as view

def find_data(search_value, data):
    for i, row in enumerate(data):
        for j, element in enumerate(row):
            if element == search_value:
                return i
    return False

def get_single_employee_data(headers, user_data):
    user = list()
    user.extend([headers, user_data])
    return user

def list_employees():
    database = hr.load_data("with-header")
    view.print_table(database)

def add_employee():
    database = hr.load_data("with-header")
    employee_data = view.get_inputs(database[0][1:])
    employee_id = [util.generate_id()]
    new_employee = employee_id + employee_data
    show_added_employee = get_single_employee_data(database[0], new_employee)
    database.append(new_employee)
    hr.save_data(database)
    view.print_table(show_added_employee)

def update_employee():
    database = hr.load_data("with-header")
    employee_id = view.get_input("Enter employee id to edit")
    find_employee = find_data(employee_id, database)
    if find_employee != False:
        employee_data = view.get_inputs(database[0][1:])
        database[find_employee][1::] = employee_data
        hr.save_data(database) 
        view.print_message(f"Employee of id: {employee_id} has been updated.")
    else:
        view.print_error_message("No employee found with provided id.")

def delete_employee():
    database = hr.load_data("header")
    employee_id = view.get_input("Enter employee id to delete")
    find_user = find_data(employee_id, database)
    if find_user != False:
        view.print_message(f"Employee id: {employee_id} deleted from the database.")
        database.remove(database[find_user])
        hr.save_data(database) 
    else:
        view.print_error_message("No employee found with provided id.")

def get_oldest_and_youngest():
    view.print_error_message("Not implemented yet.")


def get_average_age():
    view.print_error_message("Not implemented yet.")


def next_birthdays():
    view.print_error_message("Not implemented yet.")


def count_employees_with_clearance():
    view.print_error_message("Not implemented yet.")


def count_employees_per_department():
    view.print_error_message("Not implemented yet.")


def run_operation(option):
    if option == 1:
        list_employees()
    elif option == 2:
        add_employee()
    elif option == 3:
        update_employee()
    elif option == 4:
        delete_employee()
    elif option == 5:
        get_oldest_and_youngest()
    elif option == 6:
        get_average_age()
    elif option == 7:
        next_birthdays()
    elif option == 8:
        count_employees_with_clearance()
    elif option == 9:
        count_employees_per_department()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List employees",
               "Add new employee",
               "Update employee",
               "Remove employee",
               "Oldest and youngest employees",
               "Employees average age",
               "Employees with birthdays in the next two weeks",
               "Employees with clearance level",
               "Employee numbers by department"]
    view.print_menu("Human resources", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
