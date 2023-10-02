n = int(input())

costs = [list(map(int,input().split())) for _ in range(n)]

answer = float("inf")

for i in range(3):
    dp = [[float("inf")]*3 for _ in range(n+1)]
    dp[0][i] = costs[0][i]
    
    for j in range(1,n):
        dp[j][0] = min(dp[j-1][1],dp[j-1][2]) + costs[j][0]
        dp[j][1] = min(dp[j-1][0],dp[j-1][2]) + costs[j][1]
        dp[j][2] = min(dp[j-1][0],dp[j-1][1]) + costs[j][2]

    for j in range(3):
        if i != j:
            answer = min(answer,dp[n-1][j])

print(answer)