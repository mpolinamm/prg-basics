def power(x, n):
    return x ** n
if __name__ == "__main__":
    print(power(5,3))

def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)
result = power(5, 3)
print(result)
