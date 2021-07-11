def sortPara(val):
  return val[1]

def jobSequenceDeadline(arr):
  arr.sort(key = sortPara, reverse = True) # ----------------- O(nlogn)
  
  maxDeadline = max(arr)[0]
  job = [0 for i in range(maxDeadline + 1)] # ---------------- O(n)

  deadlines = {}
  for i in range(len(arr)): # -------------------------------- O(n)
    if arr[i][0] in deadlines:
      deadlines[arr[i][0]] += 1
    else:
      deadlines[arr[i][0]] = 1

  req = []
  for key in range(1, maxDeadline + 1): # -------------------- O(n)
    if key not in deadlines:
      req.append(key)
    elif deadlines[key] > 1 and len(req) > 0:
      req.pop()

  total_possible_job = maxDeadline - len(req)
  count = 0
  ans = []
  for i in range(len(arr)): # -------------------------------- O(n)
    if count >= total_possible_job:
      break
    elif job[arr[i][0]] < arr[i][0]:
      count += 1
      job[arr[i][0]] += 1
      ans.append(arr[i])

  # total_complexity = O(nlogn) + O(n) + O(n) + O(n) + O(n) => O(nlogn)
  return ans

arr = [(5, 100), (1, 19), (2, 27), (1, 25), (3, 30), (3, 28)]
# arr = [(2, 100), (1, 19), (2, 27), (1, 25), (3, 50)]
ans = jobSequenceDeadline(arr)
print(ans)