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
