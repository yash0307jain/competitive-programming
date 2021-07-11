import time
from pprint import pprint

def ratMaze(arr, row, col, ans):
  if (row == len(arr) - 1) and (col == len(arr) - 1):
    ans[row][col] = 1
    return True
  
  # bottom
  if row + 1 < len(arr):
    if (arr[row + 1][col] == 1):
      ans[row][col] = 1
      arr[row][col] = 0
      if (ratMaze(arr, row + 1, col, ans)):
        return True
      else:
        ans[row][col] = 0
        arr[row][col] = -1

  # right
  if col + 1 < len(arr):
    if (arr[row][col + 1] == 1):
      ans[row][col] = 1
      arr[row][col] = 0
      if (ratMaze(arr, row, col + 1, ans)):
        return True
      else:  
        ans[row][col] = 0
        arr[row][col] = -1

  # left
  if col - 1 >= 0:
    if (arr[row][col - 1] == 1):
      ans[row][col] = 1
      arr[row][col] = 0
      if (ratMaze(arr, row, col - 1, ans)):
        return True
      else:
        ans[row][col] = 0
        arr[row][col] = -1

  # top
  if row - 1 >= 0:
    if (arr[row - 1][col] == 1):
      ans[row][col] = 1
      arr[row][col] = 0
      if (ratMaze(arr, row - 1, col, ans)):
        return True
      else:
        ans[row][col] = 0
        arr[row][col] = -1

  return False

arr = [[1, 1, 1, 1, 1, 1],
       [1, 0, 0, 0, 0, 1],
       [1, 0, 1, 1, 0, 1],
       [1, 0, 0, 1, 1, 1],
       [1, 1, 1, 1, 0, 1],
       [0, 0, 0, 0, 0, 1]]

ans = [[0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0]]

ratMaze(arr, 0, 0, ans)
pprint(ans)