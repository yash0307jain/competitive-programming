def huffman(arr, ind, tree):
  if ind == len(arr):
    return tree

  if len(tree) == 0:
    tree.append(arr[ind])
    tree.append(arr[ind + 1])

    arr.pop(0)
    arr.pop(1)

    arr.append(tree[2])
    arr.sort()
    
    huffman(arr, ind + 2, tree)
  else:
    tree.append(arr[ind])
    tree.append(tree[len(tree) - 2] + arr[ind])

    huffman(arr, ind + 1, tree)

  return tree

arr = [5, 9, 12, 13, 16, 45]
tree = []
tree = huffman(arr, 0,  tree)
print(tree)