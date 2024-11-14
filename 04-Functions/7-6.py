def f(binary_number):
    return all(char in '01' for char in binary_number)
if __name__ == "__main__":
    print(f("101101"))
    print(f("1311a10100"))