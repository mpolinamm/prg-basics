def f(number1,number2,number3):
    largest = max(number1, number2, number3)
    smallest = min(number1, number2, number3)
    return largest - smallest
if __name__ == "__main__":
    print(f(7,4,9)) #result=5