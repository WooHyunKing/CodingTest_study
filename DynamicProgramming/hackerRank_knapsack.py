def unboundedKnapsack(k, arr):
    # Write your code here
    
    row = len(arr)
    col = k
    
    dp = [[0]*(k+1) for _ in range(row+1)]
    
    for i in range(1,row+1):
        dp[i][0] = 1
    
    for i in range(1,row+1):
        for j in range(1,col+1):
            if j >= arr[i-1]: 
                dp[i][j] = dp[i-1][j] + dp[i][j-arr[i-1]]
            else:
                dp[i][j] = dp[i-1][j]
    
    for i in range(col,-1,-1):
        if dp[row][i] != 0:
            return i