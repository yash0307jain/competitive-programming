def minCoins(arr, ind, target, collect):
  # use global only when to print minimum possible combination but make sure to remove the ans from function paramter,
  # else add a parameter ans in function if do not want to use global
  global ans

  if sum(collect) == target:
    # to print all possible collection of coins
    # return ans.append(collect)

    # to print only the minimum possible combination
    if len(ans) > len(collect) or len(ans) == 0:
      ans = collect.copy()
      return ans
    else:
      return ans

  if ind == len(arr):
    return ans

  for i in range(ind, len(arr)):
    next_ind = i
    temp = collect.copy()
    currentSum = sum(temp)

    currentCoinCount = (target - currentSum) // arr[i]
    for _ in range(currentCoinCount):
      temp.append(arr[i])
      next_ind = i + 1

      # to find all possible combinations of coins
      # minCoins(arr, next_ind, target, temp, ans)

    # while True:
    #   if (currentSum + arr[i]) <= target:
    #     temp.append(arr[i])
    #     currentSum = currentSum + arr[i]
    #     next_ind = i + 1

    #     # to find all possible combinations of coins
    #     minCoins(arr, next_ind, target, temp, ans)
    #   else:
    #     break
    
    # to find the minimum number possible combination of coins
    if(i != next_ind):
      minCoins(arr, next_ind, target, temp)

  return ans

target = 6
arr = [1, 3, 4]
ans = []

ans = minCoins(arr, 0, target, [])
# use this when not using global
# for i in range(len(ans)):
#   print(ans[i])

# use print when use global
print(ans)