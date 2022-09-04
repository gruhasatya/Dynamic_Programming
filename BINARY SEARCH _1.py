def binary_search(left, right, arr, target):
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif target < arr[mid]:
        return binary_search(left, mid - 1, arr, target)
    else:
        return binary_search(mid + 1, right, arr, target)

arr = [1,2,3,4,5,6,7,8,9,10]
target = 9
print(binary_search(0, len(arr) - 1, arr, target))