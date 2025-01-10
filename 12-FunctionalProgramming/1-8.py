name = input("Enter name: ")
surname = input("Enter surname: ")

initials = lambda name,surname: name[0] + surname[0]

print(f"Your initials are {initials(name,surname)}")