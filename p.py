# def SearchingChallenge(str):
#     # code goes here
#     str = str.split()
#     for i in range(len(str)):
#         if str[i].isnumeric():
#             str[i] = int(str[i])
#     for i in range(len(str)):
#         if str[i] == 1:
#             return str[i+1]
#     return "not found"





# substring logic is used to find the index of the first occurrence of s2 in s1 and if s2 is not found in s1 then return -1



# def substring(s1, s2):                                              # s1 is the string and s2 is the substring
#     m = len(s1)
#     n = len(s2)
#     for i in range(m):                                             # loop through the string
#         for j in range(n):                                         # loop through the substring
#             if s1[i] == s2[j]:                                     # if the character in the string is equal to the character in the substring
#                 return i                                           # return the index of the character in the string
#     return -1
#
#
#
#
# def substring(s1, s2):                                                       # s1 = "hello" and s2 = "ll"
#     m = len(s1)                                                              # m = 5
#     n = len(s2)                                                              # n = 2
#     for i in range(m):                                                       # i = 0, 1, 2, 3, 4
#         j = 0                                                                # j = 0
#         while j < n and i + j < m and s1[i + j] == s2[j]:                    # j = 0, 1, 2, 3, 4
#             j += 1                                                           # j = 1, 2
#         if j == n:                                                           # j = 2
#             return i                                                         # return 2
#     return -1                                                                # return -1
#
#
#
# if __name__ == '__main__':
#     s1 = input("Enter the first string: ")
#     s2 = input("Enter the second string: ")
#     print(substring(s1, s2))
# # testcases satsifies the following conditions:
# # 1. hello , ll
# # 2. hello , hello
# # 3. hello , llo















# def getMissingNo(A):                                    # A = [1,2,3,4,5,6,7,8,9,10]
#     total = (n + 1) * (n + 2) / 2                       # total = 11 * 12 / 2 = 66
#     sum_of_A = sum(A)                                   # sum_of_A = 55
#     return total - sum_of_A                             # return 66 - 55 = 11
#
#
# if __name__ == '__main__':
#     n = int(input("Enter the number of elements: "))                   # n = 10
#     A = list(map(int, input("Enter the elements: ").split()))          # A = [1,2,3,4,5,6,7,8,9,10]
#     miss = int(getMissingNo(A))                                        # miss = 11
#     print(miss)











# def maxloot(arr, n):                                                                 # arr = [1,2,3,4,5,6,7,8,9,10] and n = 10
#     if n == 0:                                                                       # n = 10
#         return 0                                                                     # return 0
#     if n == 1:                                                                       # n = 1
#         return arr[0]                                                                # return 1
#     if n == 2:                                                                       # n = 2
#         return max(arr[0], arr[1])                                                   # return 2
#     dp = [0] * n                                                                     # dp = [0,0,0,0,0,0,0,0,0,0]
#     dp[0] = arr[0]                                                                   # dp[0] = 1
#     dp[1] = max(arr[0], arr[1])                                                      # dp[1] = 2
#     for i in range(2, n):                                                            # i = 2, 3, 4, 5, 6, 7, 8, 9
#         dp[i] = max(arr[i] + dp[i - 2], dp[i - 1])                                   # dp[2] = 4, dp[3] = 6, dp[4] = 9, dp[5] = 12, dp[6] = 16, dp[7] = 20, dp[8] = 25, dp[9] = 30
#     return dp[-1]                                                                    # return 30
#
#
# if __name__ == '__main__':
#     n = int(input("Enter the number of elements: "))
#     arr = list(map(int, input("Enter the elements: ").split()))
#     print(maxloot(arr, n))


# def can_reach_end(nums):
#     if len(nums) == 1:
#         return True
#     max_reach = 0
#     for i in range(len(nums)):
#         if max_reach < i:
#             return False
#         max_reach = max(max_reach, i + nums[i])
#     return True



# def longest_flat(arry):
#     if len(arry) == 1:
#         return 1
#     count = 1
#     max_count = 1
#     for i in range(1, len(arry)):
#         if arry[i] == arry[i - 1]:
#             count += 1
#             max_count = max(max_count, count)
#         else:
#             count = 1
#     return max_count





# def find_mistake(nums):
#     nums.sort()
#     missing = 0
#     repeated = 0
#     for i in range(1, len(nums)):
#         if nums[i] == nums[i - 1]:
#             repeated = nums[i]
#         elif nums[i] - nums[i - 1] > 1:
#             missing = nums[i] - 1
#     return True if missing == 0 else False
#
# if __name__ == '__main__':
#     nums = list(map(int, input("Enter the elements: ").split()))
#     print(find_mistake(nums))


# def longest_flat(arry):
#     if len(arry) == 1:
#         return 1
#     count = 1
#     max_count = 1
#     for i in range(1, len(arry)):
#         if arry[i] == arry[i - 1]:
#             count += 1
#             max_count = max(max_count, count)
#         else:
#             count = 1
#     return max_count
#
# if __name__ == '__main__':
#     arr = list(map(int, input("Enter the elements: ").split()))
#     print(longest_flat(arr))


#
# def delete_distance(str1, str2):
#     m = len(str1)
#     n = len(str2)
#     dp = [[0 for x in range(n + 1)] for x in range(m + 1)]
#     for i in range(m + 1):
#         for j in range(n + 1):
#             if i == 0:
#                 dp[i][j] = j
#             elif j == 0:
#                 dp[i][j] = i
#             elif str1[i - 1] == str2[j - 1]:
#                 dp[i][j] = dp[i - 1][j - 1]
#             else:
#                 dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j])
#     return dp[m][n]
#
# if __name__ == '__main__':
#     str1 = input("Enter the first string: ")
#     str2 = input("Enter the second string: ")
#     print(delete_distance(str1, str2))



# def bracket_match(text):
#     count = 0
#     for i in range(len(text)):
#         if text[i] == '(':
#             count += 1
#         elif text[i] == ')':
#             count -= 1
#         if count < 0:
#             return 1
#     return 0 if count == 0 else -1
#
#
# if __name__ == '__main__':
#     text = input("Enter the string: ")
#     print(bracket_match(text))












# def finndMinHealth(power, armor):
#     if len(power) == 1:
#         return 1
#     dp = [0] * len(power)
#     dp[0] = 1
#     for i in range(1, len(power)):
#         if power[i] > armor[i - 1]:
#             dp[i] = 1
#         else:
#             dp[i] = dp[i - 1] + 1
#     return dp[-1]
#
#
#
# if __name__ == '__main__':
#     power = list(map(int, input("Enter the power: ").split()))
#     armor = list(map(int, input("Enter the armor: ").split()))
#     print(finndMinHealth(power, armor))

# def getMAxAggreateTemperatureChange(tempChange):
#     if len(tempChange) == 1:
#         return tempChange[0]
#     dp = [0] * len(tempChange)
#     dp[0] = tempChange[0]
#     for i in range(1, len(tempChange)):
#         dp[i] = max(tempChange[i], tempChange[i] + dp[i - 1])
#     return max(dp)
#
# if __name__ == '__main__':
#     tempChange = list(map(int, input("Enter the temperature change: ").split()))
#     print(getMAxAggreateTemperatureChange(tempChange))




# def minimumGoups(awards, k):
#     n = len(awards)
#     if n == 0:
#         return 0
#     count = 1
#     start = 0
#     for i in range(1, n):
#         if awards[i] - awards[start] > k:
#             count += 1
#             start = i
#     return count
#
#
# if __name__ == '__main__':
#     awards = list(map(int, input("Enter the awards: ").split()))
#     k = int(input("Enter the value of k: "))
#     print(minimumGoups(awards, k))

#
# def rotate_right_string(input1, input2):
#     if len(input1) != len(input2):
#         return False
#     if len(input1) == 0:
#         return True
#     for i in range(len(input1)):
#         if input1[i] == input2[0]:
#             if input1[i:] + input1[:i] == input2:
#                 return True
#     return False


# def count_of_words(input1):
#     count = 0
#     for i in range(len(input1)):
#         if input1[i] == ' ':
#             count += 1
#     return count + 1


# def getMinimumCost(parcels, k):
#     rem = len(parcels) % k
#     if rem == 0:
#         rem = k
#     parcels.sort(reverse=True)
#     cost = 0
#     for i in range(rem):
#         cost += parcels[i]
#     for i in range(rem, len(parcels), k):
#         cost += 2 * parcels[i]
#     return cost
#
#     parcels = list(map(int, input("Enter the parcels: ").split()))
#     k = int(input("Enter the value of k: "))
#     print(getMinimumCost(parcels, k))


# the interns at amazon were asked to review the company's stock value over period. given the stock price of n months , the net price change for the ith month is given by the difference between the ith month is defined as the absolute difference between the average stock price for the first i month and for remaning n-i months.
# note that these average are rounded down the integer

# the average if a set of integers here is defined as the sum of the integers divided by the number of integers, rounded down to the nearest integer . for example, the average of the set {1,2,3,4,5} is (1+2+3+4+5)/5 = 3

# the interns were asked to find the minimum number of months in which the net price change was negative. if the net price change was negative for all months, the interns were asked to find the number of months in which the net price change was the smallest

# input format
# the first line contains an integer n, the number of months
# the second line contains n space separated integers, the stock price for each month

# output format
# print the minimum number of months in which the net price change was negative. if the net price change was negative for all months, print the number of months in which the net price change was the smallest

# sample input
# 5
# 1 2 3 4 5

# sample output
# 1

# sample input
# 5
# 5 4 3 2 1

# sample output
# 5


# def result(num):
#     for num in range(1,num):
#         if num % 3 == 0:
#             print("Cheap")
#         elif num % 5 == 0:
#             print("Thrills")
#         elif num % 3 == 0 and num % 5 == 0:
#             print("CheapThrills")
#         else:
#             print(num)
#
# if __name__ == '__main__':
#     num = int(input())
#     result(num)



# write a hugo program to draw the symbol +

# def draw_symbol():
#     for i in range(5):
#         for j in range(5):
#             if i == 2 or j == 2:
#                 print("*", end="")
#             else:
#                 print(" ", end="")
#         print()
#
# if __name__ == '__main__':
#     draw_symbol()

# write a program to find the sum of the digits of a given number - sum of digits


# def sol(num):
#     sum = 0
#     while num > 0:
#         sum += num % 10
#         num //= 10
#     return sum
#
# if __name__ == '__main__':
#     num = int(input("Enter the number: "))
#     print(sol(num))


# write a program to check key present in both strings and print \

# def sol(str1, str2):
#     for i in str1:
#         if i in str2:
#             return "Yes"
#     return "No"

# number of distinct years.

# class UserMainCode(object):
#     @classmethod
#     def numberOfDistinctYears(cls, input1):
#         years = []
#         for i in input1:
#             if i[2] not in years:
#                 years.append(i[2])
#         return len(years)
#
#
#
# if __name__ == '__main__':
#     input1 = list(map(int, input("Enter the years: ").split()))
#     print(UserMainCode.numberOfDistinctYears(input1))


# a small portion contains 3 chunks. A large one contains 7 chunks
# write a program to find the number of small and large portions that can be formed from the given number of chunks

# class solution:
#     def count(self, chunks):
#         small = chunks // 3
#         large = chunks // 7
#         return small, large
#
# if __name__ == '__main__':
#     chunks = int(input("Enter the number of chunks: "))
#     print(solution().count(chunks))


# detective land
# def sol():
#     n = int(input())
#     arr = list(map(int, input().split()))
#     count = 0
#     for i in range(n):
#         if arr[i] == 0:
#             count += 1
#     return count
#
# if __name__ == '__main__':
#     print(sol())


# explqanation
# n1 = 11, n2 = 23
# prime numbers between 11 and 23 are 11, 13, 17, 19
# exclude n2 = 23
# 11, 13, 17, 19 should be there in the output
# largest prime number is 19. difference between 19 and 11 is 8. so the output is 8
# difference between 19 and 13 is 6. so the output is 6
# difference between 19 and 17 is 2. so the output is 2
# sum of difference is 16. so the output is 16

# def solution(n1, n2):                      # 11, 23
#     prime = []                             # [11, 13, 17, 19]
#     for i in range(n1, n2):                # 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22
#         if i > 1:                          # 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22
#             for j in range(2, i):          # 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21
#                 if i % j == 0:             # 11 % 2 == 0, 11 % 3 == 0, 11 % 4 == 0, 11 % 5 == 0, 11 % 6 == 0, 11 % 7 == 0, 11 % 8 == 0, 11 % 9 == 0, 11 % 10 == 0, 11 % 11 == 0
#                     break
#             else:                          # 11, 13, 17, 19
#                 prime.append(i)            # [11, 13, 17, 19]
#     diff = []                              # [8, 6, 2]
#     for i in range(len(prime)):            # 0, 1, 2, 3
#         diff.append(prime[-1] - prime[i])  # 19 - 11, 19 - 13, 19 - 17, 19 - 19
#     return sum(diff)                       # 8 + 6 + 2 = 16
#
# if __name__ == '__main__':
#     n1 = int(input("Enter the value of n1: "))
#     n2 = int(input("Enter the value of n2: "))
#     print(solution(n1, n2))


# group the array of elements based on the first sequence of elements

# def rearrange(arr):                                                              # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     map = {}                                                                     # {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10}
#     for i in arr:                                                                # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
#         map[i] = map.get(i, 0) + 1                                               # {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1}
#     for i in arr:
#         if map.get(i):
#             for _ in range(map[i]):                                              # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
#                 print(i, end=' ')                                                # 1 2 3 4 5 6 7 8 9 10
#             map[i] = 0                                                           # {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}
#
# if __name__ == '__main__':
#     arr = list(map(int, input().split()))
#     rearrange(arr)


# def sol(n):
#     for i in range(n):
#         for j in range(n - i):
#             print(" ", end="")
#         for k in range(2*i + 1):
#             print("*", end="")
#         print()
#
# def sol1(n):
#     for i in range(n):
#         for j in range(n-1):
#             print(" ", end="")
#         print("* * *", end="")
#
# if __name__ == '__main__':
#     n = int(input())
#     sol(n)
#     sol1(n)
#     sol(n)

class Soltion:
    # def subArraySum(self, arr, n, s):
    #     for i in range(n):
    #         for j in range(i, n):
    #             if sum(arr[i:j+1]) == s:
    #                 return i+1, j+1
    #     return -1

    # //////////////////////////////////////////////////////////////////
    def subArraySum(self, arr, n, s):
        start = 0
        end = 0
        sum = 0
        while end < n:
            sum += arr[end]
            while sum > s:
                sum -= arr[start]
                start += 1
            if sum == s:
                return start+1, end+1
            end += 1
        return -1

# /////////////////////////////////////////////////////////////

class Solution:
    def subArraySum(self, arr, n, s):                                        # [1, 2, 3, 7, 5], 5, 12                                                             # 1, 2, 3, 7, 5                                 # 1, 2, 3, 7, 5
        begin = 0                                                           # Two pointers
        end = 0                                                            # begin = 0, end = 0

        curr_sum = arr[begin]                                              # sum start from 1                                                                     # 1
        while begin != n:                                                  # while begin which is  not less  then (0 != 5) goes on                                # 0 != 5
            if curr_sum == s:                                              # if sum is equal to 12                                                                # 1 == 12
                return begin + 1, end + 1                                  # return the value ecluding 0                                                          # 1, 1
            elif curr_sum < s and end < n - 1:                             # if sum is less than 12 and end is less than 4 which is 5                             # 1 < 12 and 0 < 4
                end += 1                                                   # increment end by 1                                                                   # 1
                curr_sum += arr[end]                                       # add the value of end to curr_sum                                                     # 1 + 2
            elif begin == end and end < n - 1:                             # if begin is equal to end and end is less than 4                                      # 0 == 0 and 0 < 4
                end += 1                                                   # increment end by 1                                                                   # 1
                curr_sum += arr[end]                                       # add the value of end to curr_sum                                                     # 1 + 2
            else:
                curr_sum -= arr[begin]                                     # subtract the value of begin from curr_sum                                            # 1 - 1
                begin += 1                                                 # increment begin by 1                                                                 # 1
        return [-1]


if __name__ == '__main__':
    arr = list(map(int, input().split()))
    s = int(input())
    print(Soltion().subArraySum(arr, len(arr), s))

