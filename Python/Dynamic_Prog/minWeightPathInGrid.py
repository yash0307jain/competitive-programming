def minWeightPath(arr, x, y):
  

# arr = [[3, 7, 9, 2, 7],
#        [9, 8, 3, 5, 5],
#        [1, 7, 9, 8, 5],
#        [3, 8, 6, 4, 10],
#        [6, 3, 9, 7, 8]]

arr = [[3, 7, 9],
       [9, 8, 3],
       [1, 7, 9]]
path = [(0, 0)]
sum = {}

sum = minWeightPath(arr, 0, 0)
# print(path)
# print(sum)