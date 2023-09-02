t = int(input())

answer = []

for _ in range(t):
    n = int(input()) // 10

    dp = [0]*301

    dp[1], dp[2] = 1, 3

    if 1 <= n <= 2:
        answer.append(dp[n])
    else:
        for i in range(3,n+1):
            dp[i] = dp[i-1] + 2*dp[i-2]
        answer.append(dp[n])

for i,value in enumerate(answer):
    print(f"#{i+1} {value}")