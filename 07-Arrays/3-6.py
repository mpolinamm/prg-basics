array = [
   [0, 0, 0],
   [0, 0, 0],
   [0, 0, 0]
]

for i in range(len(array)): 
   array[i][i] = 1 

for row in array:
   print(" ".join(map(str, row)))