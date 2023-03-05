import sys
input = sys.stdin.readline

n = int(input())

triangle = []
dp = [[0]*n for i in range(n)]

for i in range(n):
    triangle.append(list(map(int,input().split())))

dp[0][0] = triangle[0][0]

for i in range(1,n):
    for j in range(i+1):
        if i == 0 :
            dp[i][j] = triangle[i][j] + dp[i-1][j]
        elif j == i :
            dp[i][j] = triangle[i][j] + dp[i-1][j-1]
        else:
            dp[i][j] = triangle[i][j] + max(dp[i-1][j],dp[i-1][j-1])

print(max(dp[n-1]))