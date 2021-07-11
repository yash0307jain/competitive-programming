import time
count = 0

def isSafe(arr, row, col):
  for i in range(0, col):
    if(arr[row][i] == '1'):
      return False

  for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
    if(arr[i][j] == '1'):
      return False
  
  for i, j in zip(range(row, len(arr)), range(col, -1, -1)):
    if(arr[i][j] == '1'):
      return False
  
  return True

def nQueen(arr, col):
  global count

  if col >= len(arr):
    return True
  
  for i in range(0, len(arr)):
    count = count + 1
    if(isSafe(arr, i, col)):
      arr[i][col] = '1'
      if(nQueen(arr, col + 1)):
        return True
      else:
        arr[i][col] = '.'

  return False

N = 8
arr = []
for i in range(N):
  temp = []
  for j in range(N):
    temp.append('.')
  arr.append(temp)

if nQueen(arr, 0) == False:
  print("Solution not exist")
else:
  for i in range(len(arr)):
    print(arr[i])

print("Count -> ", count)