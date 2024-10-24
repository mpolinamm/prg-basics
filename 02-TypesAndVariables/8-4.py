height_cm = float(input("Enter your height in centimeters: "))
cm_inches =2.54
inches_in_feet = 12
height_inches = height_cm / cm_inches
feet = int(height_inches // inches_in_feet) 
inches = int(height_inches % inches_in_feet) 
print(f'I am {height_cm:.2f} cm tall, i.e. {feet} feet and {inches} inches')

