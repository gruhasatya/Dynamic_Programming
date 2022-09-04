# Find the number of rotations in a circularly sorted array

def count_rotations(arr):
    n = len(arr)

    min_index = 0
    min = arr[0]
    for i in range(0,n):
        if arr[i] < min:
            min = arr[i]
            min_index = i
    return min_index

arr = [15, 18, 2, 3, 6, 12]
print(count_rotations(arr))




##########################################        Binary search        ##########################################

def count_rotation(arr, target, left, right):
    while left <= right:
        if arr[left] <= arr[right]:
            return left
        mid = (left + right) // 2
        prev = (mid - 1 + n) % n
        next = (mid + 1) % n
        if arr[mid] <= arr[prev] and arr[mid] <= arr[next]:
            return mid
        elif arr[mid] <= arr[right]:
            right = mid - 1
        elif arr[mid] >= arr[left]:
            left = mid + 1
    return -1

arr = [15, 18, 2, 3, 6, 12]
n = len(arr)
print(count_rotation(arr, 0, 0, n - 1))