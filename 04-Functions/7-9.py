def f(x,y):
    return sum(1 for i in range(x + 1, y) if i < 0 and i % 2 == 0)
if __name__ == "__main__":
    print(f(-7,8))

def f(x, y):
    count = 0
    for i in range(x + 1, y):
        if i < 0 and i % 2 == 0:
            count += 1
    return count
if __name__ == "__main__":
    print(f(-7,8))