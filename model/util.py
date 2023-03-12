import random
import string

def get_random_letters(number, size = "upper"):
    alphabet = string.ascii_lowercase if size == "lower" else string.ascii_uppercase
    random_letters = list()
    for i in range(number):
       random_letters.append(alphabet[random.randint(0, len(alphabet) - 1)])
    return random_letters

def get_random_digits(number):
    random_digits = list()
    for i in range(number):
       random_digits.append(str(random.randint(0, 9)))
    return random_digits

def get_random_special_characters(number, special_characters_list):
    random_special_characters = list()
    for i in range(number):
        random_special_characters.append(special_characters_list[random.randint(0, len(special_characters_list) - 1)])
    return random_special_characters

def get_shuffled_string_id(id_characters_list):
    new_id = sum(id_characters_list, [])
    random.shuffle(new_id)
    return "".join(new_id)

def generate_id(number_of_small_letters=4,
                number_of_capital_letters=2,
                number_of_digits=2,
                number_of_special_chars=2,
                allowed_special_chars=r"_+-!"):
    random_characters = list()
    number_of_small_letters > 0 and random_characters.append(get_random_letters(number_of_small_letters, "lower"))
    number_of_capital_letters > 0 and random_characters.append(get_random_letters(number_of_capital_letters, "upper"))
    number_of_digits > 0 and random_characters.append(get_random_digits(number_of_digits))
    number_of_special_chars > 0 and random_characters.append(get_random_special_characters(number_of_special_chars, allowed_special_chars))
    new_id = get_shuffled_string_id(random_characters)
    return new_id