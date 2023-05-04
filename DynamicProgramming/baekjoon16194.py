n = int(input())
data = list(map(int,input().split()))

p_count = len(data)

dp = [[0]*(n+1) for _ in range(p_count+1)]

for i in range(1,n+1):
    dp[1][i] = data[0]*i

for i in range(2,p_count+1):
    for j in range(1,n+1):
        if i > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = min(dp[i-1][j], data[i-1] + dp[i][j-i])

print(dp[p_count][n])