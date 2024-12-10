def print_unique_elements(array):
    count = {}
    
    for num in array:
        count[num] = count.get(num, 0) + 1
    
    unique_elements = [num for num, cnt in count.items() if cnt == 1]
    
    print("Unique elements:", " ".join(map(str, unique_elements)))

array = [2, 3, 2, 5, 8, 1, 9, 8]

print_unique_elements(array)
