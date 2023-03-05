n = int(input())

score = [0]*n
dp = [0]*n

for i in range(n):
    score[i] = int(input())

if n == 1:
    print(score[0])
elif n == 2:
    print(score[0]+score[1])
elif n == 3:
    print(score[0]+max(score[1],score[2]))
else:
    dp[0] = score[0]
    dp[1] = score[0] + score[1]
    dp[2] = score[2] + max(score[1],score[0])
    
    for i in range(3,n):
        dp[i] = score[i] + max(score[i-1] + dp[i-3], dp[i-2])

    print(dp[n-1])