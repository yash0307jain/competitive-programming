from math import ceil, log2

def build(arr, start, end, tree, node):
  if start == end:
    tree[node] = arr[start]
  else:
    mid = (start + end) // 2

    build(arr, start, mid, tree, node*1 + 1)
    build(arr, mid + 1, end, tree, node*2 + 1)

    tree[node] = tree[2*node + 1] + tree[2*tree + 2]

tree = []
arr = [1, 3, 5, 7, 9, 11]

build(arr, 0, len(arr), tree, 0)