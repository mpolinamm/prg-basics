balance = 1000 
pin = '1111'

while True:
    print()
    print("ATM Menu:")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Change pin")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")
    print()

    if choice == '1':
        print(f"Your current balance is: €{balance}")
    elif choice == '2':
        amount = float(input("Enter the amount to deposit: "))
        balance += amount
        print(f"€{amount} has been deposited. New balance: €{balance}")
    elif choice == '3':
        amount = float(input("Enter the amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print(f"€{amount} has been withdrawn. New balance: €{balance}")
        else:
            print("Insufficient balance.")
    elif choice == '4':
        current_pin = input("Enter your current PIN: ")
        if current_pin == pin:
            new_pin = input("Enter a new 4-digit PIN: ")
            if len(new_pin) == 4 and new_pin.isdigit():
                pin = new_pin
                print("PIN successfully changed.")
            else:
                print("Invalid PIN. It must be exactly 4 digits.")
        else:
            print("Incorrect current PIN.")
    elif choice == '5':
        print("Exiting... Thank you for using the ATM!")
        break  
    else:
        print("Invalid option. Please try again.")