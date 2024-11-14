def f(n):
    a, b = 0, 1
    for _ in range(1, n):
        a, b = b, a + b
    return a
if __name__ == "__main__":
    print(f(5))
    print(f(9))