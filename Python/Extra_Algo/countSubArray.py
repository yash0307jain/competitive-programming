def countSubArray(arr, target):
  n = len(arr)
  answer = 0
  ele_sum = 0
  map_ele_sum = {}

  # just to set the initial value 0 (only run once per key)
  map_ele_sum.setdefault(ele_sum, 0) 
  map_ele_sum[ele_sum] += 1

  for i in range(n):
    ele_sum += arr[i]
    remove_target = ele_sum - target
    
    map_ele_sum.setdefault(remove_target, 0)
    answer += map_ele_sum[remove_target]
    
    map_ele_sum.setdefault(ele_sum, 0)
    map_ele_sum[ele_sum] += 1

  return answer

arr = [1, 3, 2, 1, 1]
target = 4

print(countSubArray(arr, target))
