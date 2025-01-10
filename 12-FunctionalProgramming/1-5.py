def avg_speed(distance,hours,minutes):
    time = hours + minutes/60
    speed = distance/time
    return speed 

distance = float(input("Enter distance in km: "))
hours = float(input("Enter number of travel hours: "))
minutes = float(input("Enter number of travel minutes: "))

print(f"Average speed: {avg_speed(distance,hours,minutes):.2f} k/h")