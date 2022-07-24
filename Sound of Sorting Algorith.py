# Selection Sort

# 1 find smallestr elemnt
# 2 swap with first element

def selection_sort(A, n):
    for i in range(n):
        min_index = i
        for j in range(i+1 , n):
            if A[j] < A[min_index]:
                min_index = j
        A[i], A[min_index] = A[min_index], A[i]
    return  A    # return to print(A) to run the program

if __name__ =="__main__":
  selection_sort([64,25,12,22,11],5)





# inserion Sort

# 1 A(1) is sorted
# 2 find right position of j
# 3 move larger elements to right

def inserion_sort(A, n):
    for i in range(1, n):                  # start from 1 element
        j = i                              # j is the index of the element to be inserted
        while j > 0 and A[j-1] > A[j]:     # while j is not the first element and A[j-1] is larger than A[j]
            A[j], A[j-1] = A[j-1], A[j]
            j -= 1                         # move j to the left
    return A

if __name__=="__main__":
  inserion_sort([12, 11, 13, 5, 6,9,21,36], 8)


# Merge sort

# 1 Split the array into two halves
# 2 Sort the two halves
# 3 Merge the two sorted halves into one sorted array

def Merge_sort(A, n):
    if n > 1:
        mid = n // 2
        L = A[:mid]
        R = A[mid:]
        Merge_sort(L, len(L))
        Merge_sort(R, len(R))
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            A[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            A[k] = R[j]
            j += 1
            k += 1
    return A



# Bubble Sort

# 1 compare adjacent elements
# 2 if they are not in order, swap them
# 3 repeat until no swaps are made in a pass through the list

def Bubble_sort(A, n):
    for i in range(n):
        for j in range(0, n-i-1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
    return A


