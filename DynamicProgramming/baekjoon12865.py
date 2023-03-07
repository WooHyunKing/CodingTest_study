n, k = map(int,input().split())

list = [(0,0)]

for i in range(n):
    list.append(tuple(map(int,input().split())))

dp = [[0] * (k+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1, k+1):
        w = list[i][0]
        v = list[i][1]
        if j < w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j-w] + v,dp[i-1][j] )

print(dp[n][k])