time = int(input("Enter number of hours of parking: "))
if time <= 2:
    print(f"Your parking fee is 5 PLN")
elif time <= 6:
    print(f"Your parking fee is 15 PLN")
elif time > 6:
    print(f"Your parking fee is 20 PLN")