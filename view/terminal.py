COLORS = {"yellow": "\u001b[33m", "green": "\u001b[32m", "blue": "\u001b[34m", "red": "\u001B[31m", "cyan": "\u001B[36m", "color_reset": "\u001b[0m"}
BOLD_TEXT = {"begin": "\033[1m", "end": "\033[0m"}

def get_columns_width(table, padding = 0):
    columns_width = list([max(map(len, column)) for column in zip(*table)])
    return list(map(lambda column: column + 2*padding, columns_width))

def get_row_width(columns_width, number_of_columns):
    return columns_width + number_of_columns + 1

def get_column_format(columns_width, separator):
    start, end = [separator] * 2
    return start + separator.join("{{:^{}}}".format(width) for width in columns_width) + end

def print_horizontal_line(row_width, separator):
    print(separator * row_width)

def print_menu_header():
    print(f"{COLORS['yellow']}" + "=" * 40 + f"{COLORS['color_reset']}")
    print(f"{COLORS['green']}" + "{:^40}".format("CUSTOMERS SYNC LIMITED COMPANY"))
    print("{:^40}".format("--- Internal Data System ---"))
    print(f"{COLORS['cyan']}" + "{:^40}".format("PERSONAL TERMINAL"))
    print(f"{COLORS['yellow']}" + "=" * 40 + f"{COLORS['color_reset']}")

def print_result_header():
    print(f"\n\n\n{BOLD_TEXT['begin']}{COLORS['blue']}" + "-" * 19)
    print(":.:. SYSTEM ANSWER:")
    print("-" * 19 + f"{COLORS['color_reset']}")

def print_menu(title, list_options):
    print_menu_header()
    print(f"{BOLD_TEXT['begin']}{ title }:{BOLD_TEXT['end']}")
    for i in range(1, len(list_options)):
        print(f"{COLORS['yellow']}({i}){COLORS['color_reset']} { list_options[i] }")
    print(f"{COLORS['yellow']}(0){COLORS['color_reset']} { list_options[0] }")

def print_message(message):
    print_result_header()
    print(f"{BOLD_TEXT['begin']}{COLORS['green']}{message}{COLORS['color_reset']}{BOLD_TEXT['end']}")

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
    elif isinstance(result, tuple):
        show_results = '; '.join(result)
        print(f"{label}:\n{show_results}")
    elif isinstance(result, dict):
        print(f"{label}")
        for key, value in result.items():
            print(key,": ", value, sep="")
    else:
        print(f"{label}: {result:.2f}")

def print_table(table):
    print_result_header()
    columns_width = get_columns_width(table, 1)
    row_width = get_row_width(sum(columns_width), len(table[0]))
    column_format = get_column_format(columns_width, "|")
    for row in table:    
        print_horizontal_line(row_width, "-")
        print(column_format.format(*row))
    print_horizontal_line(row_width, "-")

def get_input(label):
    user_input = input(f"{ label }: ")
    return user_input

def get_inputs(labels):
    user_inputs = list()
    for label in labels:
        user_input = input(f"Enter {label}: ")
        user_inputs.append(user_input)
    return user_inputs

def print_error_message(message):
    print_result_header()
    print(f"{BOLD_TEXT['begin']}{COLORS['red']}{message}{COLORS['color_reset']}{BOLD_TEXT['end']}")