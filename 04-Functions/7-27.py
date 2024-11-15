def f(dice):
    if not dice:
        return 0
    max_count = 1  
    current_count = 1 
    prev_roll = dice[0]
    for i in range(1, len(dice)):
        if dice[i] == prev_roll:
            current_count += 1
        else:
            prev_roll = dice[i]
            current_count = 1
        max_count = max(max_count, current_count)
    return max_count
if __name__ == "__main__":
    print(f("2133")) 