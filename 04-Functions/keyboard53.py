# keyboard53.py
# Functions to read any data type from the keyboard

def input_string(message):
    user_input = input(message)
    return user_input

def input_integer(message):
    while True:
        try:
            user_input = int(input(message))
            return user_input
        except ValueError:
            print("Invalid input. Please enter an integer.")

def input_real(message):
    while True:
        try:
            user_input = float(input(message))
            return user_input
        except ValueError:
            print("Invalid input. Please enter a real number.")

def input_boolean(message):
    while True:
        user_input = input(message).strip().lower()
        if user_input in ['y', 'yes']:
            return True
        elif user_input in ['n', 'no']:
            return False
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
