def lis(arr):
  count = 0
  longSub = [arr[0]]

  for i in range(1, len(arr)):
    print(longSub)
    if longSub[len(longSub) - 1] < arr[i]:
      count += 1
      longSub.append(arr[i])
    else:
      for j in range(len(longSub)):
        count += 1
        if arr[i] <= longSub[j]:
          longSub[j] = arr[i]
          break

  print(count)
  return longSub

# arr = [1, 2, 7, 3]
# arr = [2, 3, 5, 7, 8, 4, 5, 6, 7]
# arr = [6, 2, 5, 1, 7, 4, 8, 3, 4, 5, 6, 7]
arr = [6, 2, 3, 5, 1, 7, 4, 8, 3, 4, 5, 6, 7]
# arr = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15, 16, 4]

ans = lis(arr)
print(ans)

