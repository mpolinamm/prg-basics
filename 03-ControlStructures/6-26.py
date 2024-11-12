correct_pin = '0805'
max_attempts = 3
for attempt in range(1, max_attempts + 1):
    entered_pin = input(f"Attempt {attempt}/{max_attempts} - Enter PIN code: ")
    if entered_pin == correct_pin:
        print("Correct PIN!")
        break
    else:
        print("Incorrect...")
    if attempt == max_attempts:
        print("Sorry, your payment card has been blocked.")

