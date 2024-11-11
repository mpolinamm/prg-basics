age = int(input("How old are you?: "))
if age < 13:
    print("You are a child")
elif age <= 19:
    print("You are a teen")
elif age <= 64:
    print("You are a adult")
elif age >= 65:
    print("You are a senior")