def reverse_Iterative(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr

def reverse_recursive(arr, start, end):
    if start >= end:
        return arr
    arr[start], arr[end] = arr[end], arr[start]
    return reverse_recursive(arr, start+1, end-1)


def reverse_slicing(arr):
    print(arr[::-1])
