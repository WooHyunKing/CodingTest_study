import sys
input = sys.stdin.readline

n = int(input())

prices = [list(map(int,input().split())) for _ in range(n)]

dp = [[0]*3 for _ in range(n)]

dp[0][0], dp[0][1], dp[0][2] = prices[0][0],prices[0][1],prices[0][2]

for i in range(1,n):
    for j in range(3):
        if j == 0:
            dp[i][j] = min(dp[i-1][1],dp[i-1][2]) + prices[i][j]
        elif j == 1:
            dp[i][j] = min(dp[i-1][0],dp[i-1][2]) + prices[i][j]
        elif j == 2:
            dp[i][j] = min(dp[i-1][0],dp[i-1][1]) + prices[i][j]

print(min(dp[-1]))


# area = [[0]*3 for _ in range(n)]
# dp = [[0]*3 for _ in range(n)]

# for i in range(n):
#     area[i] = list(map(int,input().split()))

# dp[0] = area[0]

# for i in range(1,n):
#     for j in range(3):
#         if j == 0:
#             dp[i][j] = area[i][j] + min(dp[i-1][1], dp[i-1][2])
#         elif j == 1:
#             dp[i][j] = area[i][j] + min(dp[i-1][0], dp[i-1][2])
#         else:
#             dp[i][j] = area[i][j] + min(dp[i-1][0], dp[i-1][1])

# print(min(dp[n-1]))