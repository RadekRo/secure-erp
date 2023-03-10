COLORS = {"yellow": "\u001b[33m", "green": "\u001b[32m", "blue": "\u001b[34m", "color_reset": "\u001b[0m"}
BOLD_TEXT = {"begin": "\033[1m", "end": "\033[0m"}

def get_list_of_max_columns_width(table, padding):
    calculate_max_columns_width = [max(map(len, column)) for column in zip(*table)]
    add_padding_to_column = map(lambda x: x + 2*padding, calculate_max_columns_width)
    return list(add_padding_to_column)

def print_menu_header():
    print(f"""{COLORS['yellow']}========================================{COLORS['color_reset']}
{COLORS['green']}     CUSTOMERS SYNC LIMITED COMPANY{COLORS['color_reset']}
{COLORS['green']}      --- Internal Data System --- {COLORS['color_reset']}
{COLORS['yellow']}========================================{COLORS['color_reset']}""")

def print_result_header():
    print(f"""\n\n{COLORS['blue']}========================================{COLORS['color_reset']}
{COLORS['blue']}         YOUR OPERATION RESULT{COLORS['color_reset']}
{COLORS['blue']}========================================{COLORS['color_reset']}""")

def print_menu(title, list_options):
    """Prints options in standard menu format like this:

    Main menu:
    (1) Store manager
    (2) Human resources manager
    (3) Inventory manager
    (0) Exit program

    Args:
        title (str): the title of the menu (first row)
        list_options (list): list of the menu options (listed starting from 1, 0th element goes to the end)
    """
    print_menu_header()
    print(f"{BOLD_TEXT['begin']}{ title }:{BOLD_TEXT['end']}")
    for i in range(1, len(list_options)):
        print(f"{COLORS['yellow']}{i}.{COLORS['color_reset']} { list_options[i] }")
    print(f"{COLORS['yellow']}0.{COLORS['color_reset']} { list_options[0] }")


def print_message(message):
    """Prints a single message to the terminal.

    Args:
        message: str - the message
    """
    pass


def print_general_results(result, label):
    """Prints out any type of non-tabular data.
    It should print numbers (like "@label: @value", floats with 2 digits after the decimal),
    lists/tuples (like "@label: \n  @item1; @item2"), and dictionaries
    (like "@label \n  @key1: @value1; @key2: @value2")
    """
    print_result_header()
    if isinstance(result, list):
        show_results = ', '.join(result)
        print(f"{label}:\n{show_results}")

# /--------------------------------\
# |   id   |   product  |   type   |
# |--------|------------|----------|
# |   0    |  Bazooka   | portable |
# |--------|------------|----------|
# |   1    | Sidewinder | missile  |
# \-----------------------------------/
def print_table(table):
    """Prints tabular data like above.

    Args:
        table: list of lists - the table to print out
    """
    print_result_header()
    # s = [[str(e) for e in row] for row in table]
    # lens = [max(map(len, col)) for col in zip(*s)]
    # fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    # new_table = [fmt.format(*row) for row in s]
    # print('\n'.join(new_table))
    count_max_columns_width = get_list_of_max_columns_width(table, 1)
    print(count_max_columns_width)

def get_input(label):
    """Gets single string input from the user.

    Args:
        label: str - the label before the user prompt
    """
    user_input = input(f"{ label }: ")
    return user_input


def get_inputs(labels):
    """Gets a list of string inputs from the user.

    Args:
        labels: list - the list of the labels to be displayed before each prompt
    """
    pass


def print_error_message(message):
    """Prints an error message to the terminal.

    Args:
        message: str - the error message
    """
    pass
