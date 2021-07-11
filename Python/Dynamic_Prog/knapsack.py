def convertToArrayOfTuple(weight, value):
  tupleArr = []

  for i in range(len(weight)):
    tupleArr.append((weight[i], value[i]))

  return tupleArr

def sortPara(val):
  return val[1]

def knapsack(weight, value, target):
  arr = convertToArrayOfTuple(weight, value)

  # arr.sort(key = sortPara, reverse = True)

  items = knapsackRecur(arr, 0, [], [], [],  target)
  print(items)
  # answer = []
  # for i in range(len(items)):
  #   sum = 0
  #   for j in range(len(items[i])):
  #     sum += items[i][j]
  #   answer.append(sum)
  # print(answer)


def knapsackRecur(arr, ind, subWeight, subValue, store, target):
  if ind == len(arr):
    return store

  for i in range(ind, len(arr)):
    valueSub = 0
    
    if len(subWeight) == 0:
      valueSub = 0
    else:
      valueSub = subWeight[len(subWeight) - 1]

    if (valueSub + arr[i][0]) <= target:
      tempWeight = subWeight.copy()
      valueTempWeight = 0

      if len(tempWeight) == 0:
        valueTempWeight = 0
      else:
        valueTempWeight = tempWeight[len(tempWeight) - 1]

      tempWeight.append(valueTempWeight + arr[i][0])

      tempValue = subValue.copy()
      valueTempValue = 0

      if len(tempValue) == 0:
        valueTempValue = 0
      else:
        valueTempValue = tempValue[len(tempValue) - 1]

      tempValue.append(valueTempValue + arr[i][1])

      store.append(tempValue)
      knapsackRecur(arr, i + 1, tempWeight, tempValue, store, target)

  return store

weight = [20, 10, 30]
value = [100, 60, 120]
knapsack(weight, value, 50)