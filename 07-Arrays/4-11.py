def compare(array1, array2):
    if len(array1) != len(array2):
        return False
    for i in range(len(array1)):
        if array1[i] != array2[i]:
            return False
    return True

arrays_to_compare = [
    (["water", "book", "sky"], ["water", "book", "sky"]),
    ([True, False], [True, False, True]),
    ([5, 3, 1], [5, 3, 1]),
    ([3, 2, 1], [3, 2])
]

for array1, array2 in arrays_to_compare:
    result = compare(array1, array2)
    comparison_result = "arrays are the same" if result else "arrays are different"
    print(f"Array1: {' '.join(map(str, array1))}")
    print(f"Array2: {' '.join(map(str, array2))}")
    print(f"Comparison: {comparison_result}\n")
