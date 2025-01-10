n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))

mean = lambda x,y: (x+y)/2


result = mean(n1,n2)
print(f"The arithmetic mean of the numbers {n1} and {n2} is {result}")