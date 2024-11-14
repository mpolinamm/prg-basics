def f(amount_to_pay):
    coins = 0
    for coin in [5, 2, 1]:
            coins += amount_to_pay // coin
            amount_to_pay %= coin
    return coins
if __name__ == "__main__":
    print(f(23))
    print(f(8))