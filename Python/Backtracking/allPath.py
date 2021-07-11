from copy import deepcopy

def allPath(arr, n, m, row, col):
  if (row == n - 1) and (col == m - 1):
    return ans.append(arr)

  # bottom
  if (row + 1 < n) and (col < m):
    new_arr = deepcopy(arr)
    new_arr[row + 1][col] = 1
    allPath(new_arr, n, m, row + 1, col)
  
  # right
  if (row < n) and (col + 1 < m):
    new_arr = deepcopy(arr)
    new_arr[row][col + 1] = 1
    allPath(new_arr, n, m, row, col + 1)

n, m = 3, 2
arr = []
for i in range(0, n):
  temp = []
  for j in range(0, m):
    temp.append(0)
  arr.append(temp)

arr[0][0] = 1
ans = []

allPath(arr, n, m, 0, 0)
for i in range(len(ans)):
  for j in range(len(ans[i])):
    print(ans[i][j])
  print()