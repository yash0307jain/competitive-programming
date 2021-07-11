def two_Sum(arr, target):
  mem = {arr[0]}

  for i in range(1, len(arr)):
    print(mem)
    subt = target - arr[i]
    if subt in mem:
      return [subt, arr[i]]
    else:
      mem.add(arr[i])

  return -1

arr = [5, 4, 1, 5, 3, 7, 10, 8, 12]
target = 4

ans = two_Sum(arr, target)
print(ans)