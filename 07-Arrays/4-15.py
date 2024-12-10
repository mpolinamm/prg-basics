def occurs(number, array):
    return number in array

def main():
    array = [15, 38, 7, 23, 14]
    
    number = int(input("Enter a number: "))
    
    print("Array:", " ".join(map(str, array)))
    
    if occurs(number, array):
        print(f"Result: number {number} appears in the array")
    else:
        print(f"Result: number {number} does not appear in the array")

main()
