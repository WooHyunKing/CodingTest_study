n, k = map(int,input().split())

info = [[0,0]] + [list(map(int,input().split())) for _ in range(n)]

dp = [[0]*(k+1) for _ in range(n+1)]

for i in range(1,n+1):

    weight = info[i][0]
    value = info[i][1]

    for j in range(1,k+1):
        if j >= weight:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight]+value)
        else:
            dp[i][j] = dp[i-1][j]

print(max(dp[-1]))

# list = [(0,0)]

# for i in range(n):
#     list.append(tuple(map(int,input().split())))

# dp = [[0] * (k+1) for _ in range(n+1)]

# for i in range(1,n+1):
#     for j in range(1, k+1):
#         w = list[i][0]
#         v = list[i][1]
#         if j < w:
#             dp[i][j] = dp[i-1][j]
#         else:
#             dp[i][j] = max(dp[i-1][j-w] + v,dp[i-1][j] )

# print(dp[n][k])