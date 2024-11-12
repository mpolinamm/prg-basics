time_24 = input("Enter time (24-hour format, hh:mm): ")

try:
    hours, minutes = map(int, time_24.split(":"))
    
    if hours < 0 or hours > 23 or minutes < 0 or minutes > 59:
        print("Invalid time format. Please enter a valid time.")
        exit()
    
    if hours >= 12:
        period = "pm"
    else:
        period = "am"
    
    hours_12 = hours % 12
    if hours_12 == 0:
        hours_12 = 12 
    
    print(f"Time in 12-hour format: {hours_12}:{minutes:02d} {period}")

except ValueError:
    print("Invalid time format. Please enter the time in hh:mm format.")
