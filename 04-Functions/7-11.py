def f(n):
    return "*".join(["*"] * n) if n == 1 else "/".join(["*"] * n)
if __name__ == "__main__":
    print(f(6))