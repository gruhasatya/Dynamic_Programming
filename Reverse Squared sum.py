t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.reverse()
    sum = 0
    temp = 1
    for i in range(n):
        sum += temp * (arr[i]*arr[i]) # sum of squares
        if temp < 0
            temp = 1
        else:
            temp = -1
    print(sum)









#  PRACTICAL ONE

n = [1,2,3,4,5,6,67,7,8,98,9,6,7,8,43,2,4,5]
target = 3
for i in range(len(n)):
    if target == i:
        print(i)
    else:
        print(-1)