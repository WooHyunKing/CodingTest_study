def cost(B):
    # Write your code here
    length = len(B)
    A = B.copy()
    
    dp = [[0]*2 for _ in range(length)]
    
    for i in range(1,length):
        # A[i] == B[i]인 경우
        dp[i][0] = max(abs(B[i]-B[i-1])+dp[i-1][0], abs(B[i]-1)+dp[i-1][1])
        # A[i] == 1인 경우
        dp[i][1] = max(abs(1-B[i-1])+dp[i-1][0], dp[i-1][1] )
    
    return max(dp[length-1])