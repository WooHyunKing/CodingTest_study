# 1
# 2
# 3 (2 + 1)
# 5 (3 + 2)
# 8 (5 + 3)
# 13 (8 + 5)

n = int(input())

if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    dp = [0]*(n+1)
    dp[1], dp[2] = 1, 2
    
    for i in range(3,n+1):
        dp[i] = dp[i-1] + dp[i-2]
    
    print(dp[n]%10007)



