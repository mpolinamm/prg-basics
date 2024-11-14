def f(number, even):
    digits = [int(d) for d in str(number)]
    return sum(d for d in digits if (d % 2 == 0) == even)
if __name__ == "__main__":
    print(f(3124,True))
    print(f(3124,False))