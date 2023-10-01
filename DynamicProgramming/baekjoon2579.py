n = int(input())

scores = []

for i in range(n):
    scores.append(int(input()))

if n == 1:
    print(scores[0])

else:
    dp = [[0]*2 for _ in range(n+1)]

    dp[0][0], dp[1][0], dp[1][1] = scores[0], scores[1], scores[0]+scores[1]

    for i in range(2,n):
        
        dp[i][0] = max(dp[i-2][0],dp[i-2][1]) + scores[i]
        dp[i][1] = dp[i-1][0] + scores[i]

    print(max(dp[n-1][0],dp[n-1][1]))