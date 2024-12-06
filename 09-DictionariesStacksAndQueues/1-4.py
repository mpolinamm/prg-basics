person = {
   "name": "Marek",
   "surname": "Banach",
   "age": 25,
   "hobby": ["swimming","excursions"],
   "married": True,
   "phone":{"landline":"123444321","mobile":"777888999"}
}

print('Name:')
print(person["name"])

print('Hobbies:')
for hobbies in person["hobby"]:
    print(hobbies)

print('Dictionary:')
for key, value in person.items():
    print(key,":", value)

person["surname"] = "Nowak"
person["married"] = False
person["gender"] = "male"
person["hobby"].append("bicycle")
person["phone"]["work phone"] = "313131444"

print('Dictionary2:')
for key, value in person.items():
    print(key,":", value)