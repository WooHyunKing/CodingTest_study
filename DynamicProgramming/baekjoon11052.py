n = int(input())

price = list(map(int,input().split()))

dp = [[0]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    dp[i][1] = price[0]*i
    
for i in range(2,n+1):
    for j in range(2,i+1):
        dp[i][j] = max(price[j-1]+dp[i-j][i-j],dp[i][j-1] )

print(dp[n][n])