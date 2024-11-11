age_in_dog = float(input("Enter the dog's age in human years: "))
if age_in_dog <= 2:
    age_in_human = age_in_dog * 10.5
else:
    age_in_human = (2 * 10.5) + ((age_in_dog - 2) * 4)
print(f"The dog's age in human years is: {age_in_human}")