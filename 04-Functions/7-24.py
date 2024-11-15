def f(x, y):
    total_sum = 0
    for num in range(x, y + 1):
        if num % 2 == 0 and num % 3 == 0 and num % 4 != 0:
            total_sum += num
    return total_sum
if __name__ == "__main__":
    print(f(10,30)) 