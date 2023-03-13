from model.hr import hr
from model import util
from view import terminal as view

def filter_employees_birth_years(database):
    birth_years_list = list()
    for data in database:
        birth_years_list.append(int(data[2][0:4]))
    return birth_years_list

def check_leap_year(year):
    return year%400 == 0 or (year%100 > 0 and year%4 == 0)

def switch_birthday_to_year_day(string):
    year_day = 0
    year_days_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    birth_date = string.split("-")
    year, month, day = list(map(int, birth_date)) 
    year_days_list[1] = 29 if check_leap_year(year) else 28 
    if month == 1:
        year_day = day
    else:
        year_day = sum(year_days_list[:month - 1]) + day
    return year_day

def get_birthday_list(start_date):
    birthday_list = list()
    birthday = switch_birthday_to_year_day(start_date)
    for i in range (1, 15):
        birthday += 1
        if birthday > 365:
            birthday = 1
        birthday_list.append(birthday)
    return birthday_list

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
    database = hr.load_data("with-header")
    employee_id = view.get_input("Enter employee id to delete")
    find_employee = find_data(employee_id, database)
    if find_employee != False:
        view.print_message(f"Employee id: {employee_id} deleted from the database.")
        database.remove(database[find_employee])
        hr.save_data(database) 
    else:
        view.print_error_message("No employee found with provided id.")

def get_oldest_and_youngest():
    database = hr.load_data()
    database.sort(key = lambda inner:inner[2])
    oldest_youngest = (database[0][1], database[-1][1])
    view.print_general_results(oldest_youngest, "OLDEST AND YOUNGEST EMPLOYEES ARE")

def get_average_age():
    database = hr.load_data()
    employees_birth_years = filter_employees_birth_years(database)
    current_date = view.get_input("Enter current date in format (YYYY-MM-DD)")
    count_employees = len(employees_birth_years)
    average_age = ((int(current_date[0:4]) * count_employees) - sum(employees_birth_years)) / count_employees
    view.print_general_results(average_age, "AVERAGE EMPLOYEES AGE")

def next_birthdays():
    birthday_in_14_days = list()
    database = hr.load_data()
    for i in range (len(database)):
        database[i][2] = switch_birthday_to_year_day(database[i][2])
    current_date = view.get_input("Enter current date in format (YYYY-MM-DD)")
    birthday_list = get_birthday_list(current_date)
    for i in range (len(database)):
        database[i][2] in birthday_list and birthday_in_14_days.append(database[i][1])
    if len(birthday_in_14_days) > 0:
        view.print_general_results(birthday_in_14_days, "EMPLOYEES WITH BIRTHDAY IN 14 DAYS")
    else:
        view.print_message("NO EMPLOYEES WILL HAVE BIRTHDAY WITHIN 14 DAYS.")

def count_employees_with_clearance():
    database = hr.load_data()
    employees_counter = 0
    for i in range(len(database)):
        if int(database[i][4]) > 0:
            employees_counter += 1 
        else:
            None
    view.print_general_results(employees_counter, "EMPLOYEES WITH MINIMUM LEVEL 1 CLEARANCE")

def count_employees_per_department():
    database = hr.load_data()
    departments_employees = dict()
    for i in range(len(database)):
        if database[i][3] in departments_employees:
            departments_employees[database[i][3]] += 1
        else:
            departments_employees[database[i][3]] = 1
    view.print_general_results(departments_employees, "EMPLOYEES NUMBER IN EACH DEPARTMENT")

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
