def three_Sum(arr, target):
  mem = {arr[0]}

  for j in range(1, len(arr)):
    for i in range(j + 1, len(arr)):
      print(mem)
      subt = target - arr[i] - arr[j]
      if subt in mem:
        return [arr[j], subt, arr[i]]
      else:
        mem.add(arr[i])

  return -1

arr = [5, 4, 1, 5, 3, 7, 10, 8, 12]
target = 10

ans = three_Sum(arr, target)
print(ans)