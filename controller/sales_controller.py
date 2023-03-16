from model.sales import sales
from view import terminal as view
from model import util

def find_data(search_value, data):
    for i, row in enumerate(data):
        for j, element in enumerate(row):
            if element == search_value:
                return i
    return False

def list_transactions():
    database = sales.load_data(1)
    view.print_table(database)

def add_transaction():
    database = sales.load_data(1)
    transaction_data = view.get_inputs(database[0][1:])
    transaction_id = [util.generate_id()]
    new_transaction = transaction_id + transaction_data
    show_transaction = list()
    show_transaction.extend([database[0], new_transaction])
    database.append(new_transaction)
    sales.save_data(database)
    view.print_table(show_transaction)

def update_transaction():
    database = sales.load_data(1)
    transaction_id = view.get_input("Enter transaction id to edit")
    find_transaction = find_data(transaction_id, database)
    if find_transaction != False:
        transaction_data = view.get_inputs(database[0][1:])
        database[find_transaction][1:5] = transaction_data[0:4]
        sales.save_data(database) 
        view.print_message(f"Transaction id: {transaction_id} updated.")
    else:
        view.print_error_message("No transaction found with provided id.")

def delete_transaction():
    database = sales.load_data(1)
    transaction_id = view.get_input("Enter transaction id to delete")
    find_transaction = find_data(transaction_id, database)
    if find_transaction != False:
        view.print_message(f"Transaction id: {transaction_id} deleted from the database.")
        database.remove(database[find_transaction])
        sales.save_data(database) 
    else:
        view.print_error_message("No transaction found with provided id.")

def get_biggest_revenue_transaction():
    current_biggest = 0
    current_transaction = None
    database = sales.load_data(0)
    for transaction in database:
        if float(transaction[3]) > current_biggest:
            current_biggest = float(transaction[3])
            current_transaction = transaction
    view.print_message(f"Transaction with id: {current_transaction[0]} is the biggest.")
        
def get_biggest_revenue_product():
    database = sales.load_data(0)
    product_dictionary = {}
    for product in database:
        product_price = float(product[3])
        product_name = product[2]
        if product_name in product_dictionary:
            product_dictionary[product_name] += product_price
        else:
            product_dictionary[product_name] = product_price
    view.print_message(f"Product: {max(product_dictionary)} had the biggest revenue.")

def count_transactions_between():
    database = sales.load_data(0)
    start_date = view.get_input("Enter start date (YYYY-MM-DD): ")
    end_date = view.get_input("Enter end date (YYYY-MM-DD): ")
    transaction_count = 0
    for transaction in database:
        transaction_date = transaction[4]
        if start_date <= transaction_date <= end_date:
            transaction_count += 1
    view.print_message(f"Number of transactions between {start_date} and {end_date}: {transaction_count}")

def sum_transactions_between():
    database = sales.load_data(0)
    start_date = view.get_input("Enter start date (YYYY-MM-DD): ")
    end_date = view.get_input("Enter end date (YYYY-MM-DD): ")
    transaction_sum = 0
    for transaction in database:
        transaction_date = transaction[4]
        if start_date <= transaction_date <= end_date:
            transaction_sum += float(transaction[3])
    view.print_message(f"Total revenue between {start_date} and {end_date}: {transaction_sum}")    

def run_operation(option):
    if option == 1:
        list_transactions()
    elif option == 2:
        add_transaction()
    elif option == 3:
        update_transaction()
    elif option == 4:
        delete_transaction()
    elif option == 5:
        get_biggest_revenue_transaction()
    elif option == 6:
        get_biggest_revenue_product()
    elif option == 7:
        count_transactions_between()
    elif option == 8:
        sum_transactions_between()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")

def display_menu():
    options = ["Back to main menu",
               "List transactions",
               "Add new transaction",
               "Update transaction",
               "Remove transaction",
               "Get the transaction that made the biggest revenue",
               "Get the product that made the biggest revenue altogether",
               "Count number of transactions between",
               "Sum the price of transactions between"]
    view.print_menu("Sales", options)

def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)

