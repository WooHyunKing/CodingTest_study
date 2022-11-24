n = int(input())

dp = [0]*(n+1)

for i in range(2,n+1):
    # 2나 3으로 나누어 떨어지지 않은 경우 무조건 1을 빼야 하기 때문
    dp[i] = dp[i-1]+1

    if i%2 == 0:
        dp[i] = min(dp[i],dp[i//2]+1)
    if i%3 == 0:
        dp[i] = min(dp[i],dp[i//3]+1)

print(dp[n])