import time

def quick_sort(arr, start, end):
  if start < end:
    pivot = partition(arr, start, end)
    print("Pivot -> ", arr[pivot])
    time.sleep(1)
    quick_sort(arr, start, pivot - 1)
    quick_sort(arr, pivot + 1, end)

def partition(arr, start, end):
  print("------------------------------")
  print("Partition -> ", arr)
  time.sleep(1)
  pivot = arr[start]
  i = start + 1

  for j in range(start + 1, end + 1):
    if arr[j] < pivot:
      print("Index -> ", j, i)
      print("Swap -> ", arr[j], arr[i])
      time.sleep(1)

      temp = arr[i]
      arr[i] = arr[j]
      arr[j] = temp

      print("Swap -> ", arr)
      time.sleep(1)

      i = i + 1
  
  print()
  print("Index -> ", start, i - 1)
  print("Swap -> ", arr[start], arr[i - 1])
  time.sleep(1)

  temp = arr[i-1]
  arr[i-1] = arr[start]
  arr[start] = temp
  
  print("Partition -> ", arr)
  time.sleep(1)
  print("------------------------------")
  return i - 1

arr = [1, 2, 3, 4, 5]
quick_sort(arr, 0, len(arr) - 1)