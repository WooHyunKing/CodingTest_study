def solution(n):
    dp = [0]*101
    dp[1], dp[2], dp[3], dp[4], dp[5] = 1, 1, 1, 2, 2

    if n<=5:
        return dp[n]

    for i in range(6,n+1):
        dp[i] = dp[i-1] + dp[i-5]
    
    return dp[n]


t = int(input())

result = []

for _ in range(t):
    n = int(input())
    result.append(solution(n))

for i in range(t):
    print(result[i])
    
