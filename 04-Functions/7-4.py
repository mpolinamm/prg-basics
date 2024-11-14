from module74 import is_in_range
try:
    number = int(input("A number: "))
    x = int(input("Enter the start of the range: "))
    y = int(input("Enter the end of the range: "))
    
    if is_in_range(number, x, y):
        print(f"Number {number} in the range <{x},{y}>: yes")
    else:
        print(f"Number {number} in the range <{x},{y}>: no")
except ValueError:
    print("Invalid input. Please enter valid integers.")