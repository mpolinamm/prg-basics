def bubblesort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

array1 = [64, 34, 25, 12, 22, 11, 90]
array2 = [3, 5, 1, 9, 8, 2, 7]
array3 = [10, 20, 15, 5, 30]

sorted_array1 = bubblesort(array1)
sorted_array2 = bubblesort(array2)
sorted_array3 = bubblesort(array3)

print("Sorted array1:", sorted_array1)
print("Sorted array2:", sorted_array2)
print("Sorted array3:", sorted_array3)
