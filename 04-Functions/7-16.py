def f(palindrome):
    return palindrome == palindrome[::-1]
if __name__ == "__main__":
    print(f("radar"))
    print(f("12-11-21"))
    print(f("book"))