from month import input_month

try:
    month_number = int(input("Enter month number: "))
    month_name = input_month(month_number)
    
    if month_name:
        print(f"The name of month {month_number} is {month_name}")
    else:
        print("Invalid month number. Please enter a number between 1 and 12.")
except ValueError:
    print("Invalid input. Please enter a valid integer.")
