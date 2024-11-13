def time_string(hours, minutes, time_format):
    if hours < 0 or hours > 23 or minutes < 0 or minutes > 59:
        return("Invalid time format. Please enter a valid time.") 
    if time_format == "24":
        return f"{hours:02}:{minutes:02}"
    else:
        period = "pm" if hours >= 12 else "am"
        hours_12 = hours % 12
        if hours_12 == 0:
            hours_12 = 12
        return f"{hours_12}:{minutes:02}{period}"
time = time_string(15, 38, '24')
print(time)
time = time_string(11, 15, '12')
print(time)
time = time_string(13, 10, '12')
print(time)