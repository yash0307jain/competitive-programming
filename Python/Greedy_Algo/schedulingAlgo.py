def schedule(arr, ind, event, ans):
  if (ind + 1) == len(arr):
    if len(event) != 0:
      return ans.append(event)
    return ans

  for i in range(ind + 1, len(arr)):
    if arr[ind][1] < arr[i][0]:
      temp = event.copy()
      if len(temp) == 0:
        temp.append(arr[ind])
      temp.append(arr[i])
      schedule(arr, i, temp, ans)
  
  schedule(arr, ind + 1, event, ans)

  return ans

arr = [(1, 3), (2, 5), (3, 9), (6, 8)]
ans = []

ans = schedule(arr, 0, [], ans)
for i in range(len(ans)):
  print(ans[i])