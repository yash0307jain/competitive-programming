def subset(arr, ind, sub, ans):
  if ind == len(arr):
    return ans

  for i in range(ind, len(arr)):
    temp = sub.copy()
    temp.append(arr[i])
    ans.append(temp)
    subset(arr, i + 1, temp, ans)

  return ans

arr = [1, 2, 3]
ans = []

ans = subset(arr, 0, [], ans)
for i in range(len(ans)):
  print(ans[i])

