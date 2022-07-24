# Dynamic Programming: Longest Common Subsequence

def LCS_dynamic(s1,s2):
    n = len(s1)
    m = len(s2)
    table = [[0 for i in range(m+1)] for j in range(n+1)]
    for i in range(n+1):
        for j in range(m+1):
            if i == 0 or j == 0:
                table[i][j] = 0
            elif s1[i-1] == s2[j-1]:
                table[i][j] = table[i-1][j-1] + 1
            else:
                table[i][j] = max(table[i-1][j],table[i][j-1])
    index =  table[n][m]
