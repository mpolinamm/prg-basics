distance = float(input("Enter distance in km: "))
hours = float(input("Enter number of travel hours: "))
minutes = float(input("Enter number of travel minutes: "))

avg_speed = lambda distance,hours,minutes: distance/(hours + minutes/60)

print(f"Average speed: {avg_speed(distance,hours,minutes):.2f} k/h")