def solution(n):

    INF = 1000000001

    dp = [INF]*(n+10)

    dp[1],dp[2],dp[3],dp[4],dp[5] = 0,0,1,0,1

    if n < 6:
        if dp[n] == 0:
            return - 1
        else:
            return dp[n]
    for i in range(6,n+1):
        if dp[i-3] != INF and dp[i-3] != 0:
            dp[i] = min(dp[i-3]+1,dp[i])
        if dp[i-3] != INF and dp[i-3] != 0:
            dp[i] = min(dp[i-3]+1,dp[i])
    
    if dp[n] == INF or dp[n] == 0:
        return -1
    else:
        return dp[n]

