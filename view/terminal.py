COLORS = {"yellow": "\u001b[33m", "green": "\u001b[32m", "color_reset": "\u001b[0m"}
BOLD_TEXT = {"begin": "\033[1m", "end": "\033[0m"}

def print_menu_header():
    print(f"""{COLORS['yellow']}=============================={COLORS['color_reset']}
{COLORS['green']}CUSTOMERS SYNC LIMITED COMPANY{COLORS['color_reset']}
{COLORS['green']} --- Internal Data System --- {COLORS['color_reset']}
{COLORS['yellow']}=============================={COLORS['color_reset']}""")

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
    print(f"{BOLD_TEXT['begin']}{title}:{BOLD_TEXT['end']}\n")
    print("""
    """)

    pass


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
    pass


def get_input(label):
    """Gets single string input from the user.

    Args:
        label: str - the label before the user prompt
    """
    pass


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
