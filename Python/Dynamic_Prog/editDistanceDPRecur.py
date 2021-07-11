from pprint import pprint

count = 0
store = []

def editDistance(str1, str2, ind1, ind2):
  global count, store
  
  if store[ind1][ind2] != -1:
    return store[ind1][ind2]

  count += 1

  if ind1 == 0:
    store[ind1][ind2] = ind2
    return ind2
  
  if ind2 == 0:
    store[ind1][ind2] = ind1
    return ind1

  if str1[ind1 - 1] == str2[ind2 - 1]:
    store[ind1][ind2] = editDistance(str1, str2, ind1 - 1, ind2 - 1)
    return store[ind1][ind2]
  
  store[ind1][ind2] = 1 + min(
    editDistance(str1, str2, ind1 - 1, ind2),
    editDistance(str1, str2, ind1 - 1, ind2 - 1),
    editDistance(str1, str2, ind1, ind2 - 1)
  )

  return store[ind1][ind2]

str1 = "sunday"
str2 = "saturday"

store = [[-1 for i in range(len(str2) + 1)] for i in range(len(str1) + 1)]

print(editDistance(str1, str2, len(str1), len(str2)))
print(count)
print(len(str1) * len(str2))