def subarray(arr, target):
  totalSum = 0
  init = 0
  end = 0
  for i in range(len(arr)):
    # print(arr[init:end], totalSum, init, end)
    if totalSum == target:
      return arr[init:end]
    elif totalSum + arr[i] <= target:
      totalSum += arr[i]
      end += 1
    else:
      totalSum += arr[i]
      end += 1

      totalSum -= arr[init]
      init += 1

  return -1
     
arr = [1, 3, 2, 5, 1, 1, 2, 3]
target = 8

ans = subarray(arr, target)
print(ans)