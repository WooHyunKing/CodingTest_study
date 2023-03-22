n = int(input())

dp = [0]*91

dp[1], dp[2] = 1, 1

if n <= 2:
    print(dp[n])

else:
    for i in range(3,n+1):
        dp[i] = dp[i-1] + dp[i-2]
    print(dp[n])