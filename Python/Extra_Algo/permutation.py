def permutation(arr, ind):
  if ind + 1 >= len(arr):
    print(arr)
    return
  for i in range (ind, len(arr)):
    new_arr = arr.copy()
    
    temp = new_arr[ind]
    new_arr[ind] = new_arr[i]
    new_arr[i] = temp
    permutation(new_arr, ind + 1)
  return
    
arr = [1, 3, 3]
permutation(arr, 0)

# def permutation(arr, store, output):
#   store[str(arr)] = True
#   output.append(arr)
#   for i in range (1, len(arr)):
#     new_arr = arr.copy()
#     temp = new_arr[0]
#     new_arr[0] = new_arr[i]
#     new_arr[i] = temp
#     if str(new_arr) in store.keys():
#       continue
#     else:
#       permutation(new_arr, store, output)
  
#   return output
    

# arr = ['a', 'b', 'c']
# store = {}
# output = []

# result = permutation(arr, store, output)
# print("Length -> ", len(result))
# for i in range(0, len(result)):
#   print(result[i])