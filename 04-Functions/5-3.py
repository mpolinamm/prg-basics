# employee_program.py
# Allows entering and printing employee data with optional salary protection

from keyboard53 import input_string, input_integer, input_real, input_boolean

def main():
    print("Enter Employee Data")

    # Reads employee's data from the keyboard
    first_name = input_string('Enter name: ')
    last_name = input_string('Enter last name: ')
    age = input_integer('Enter age: ')
    salary = input_real('Enter salary: ')
    is_salary_hidden = input_boolean('Hide salary? (y/n): ')

    # Prints employee's record
    print('\nDATA RECORD')
    print('===========')
    print(f'Name: {first_name}')
    print(f'Last name: {last_name}')
    print(f'Age: {age}')
    
    if is_salary_hidden:
        print('Salary: [Hidden]')
    else:
        print(f'Salary: ${salary:.2f}')

if __name__ == "__main__":
    main()
