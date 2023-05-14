def getWays(n, c):
    # Write your code here
    coin_count = len(c)
    
    dp = [[0]*(n+1) for _ in range(coin_count+1)]
    
    for i in range(1,coin_count+1):
        dp[i][0] = 1
        
    for i in range(1,coin_count+1):
        for j in range(1,n+1):
            coin_value = c[i-1]
            if coin_value > j :
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-coin_value]
                
    return dp[coin_count][n]