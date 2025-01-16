recorded_speeds = [48, 47, 54, 50, 42, 68, 39, 46]

speed_too_high = list(filter(lambda speed: speed > 50, recorded_speeds))

print(f"Recorded values: {', '.join(map(str, recorded_speeds))}")
print(f"Speed too high: {', '.join(map(str, speed_too_high))}")
