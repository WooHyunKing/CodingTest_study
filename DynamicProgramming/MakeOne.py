# n = int(input())

# dp = [0]*(n+1)

# for i in range(2,n+1):
#     # 2나 3으로 나누어 떨어지지 않은 경우 무조건 1을 빼야 하기 때문
#     dp[i] = dp[i-1]+1

#     if i%2 == 0:
#         dp[i] = min(dp[i],dp[i//2]+1)
#     if i%3 == 0:
#         dp[i] = min(dp[i],dp[i//3]+1)

# print(dp[n])

n = int(input())

dp = [0]*3000003

for i in range(1,n+1):
    
    if dp[i+1] == 0:
        dp[i+1] = dp[i] + 1
    else:
        dp[i+1] = min(dp[i+1], dp[i]+1)
    
    if dp[i*2] == 0:
        dp[i*2] = dp[i] + 1
    else:
        dp[i*2] = min(dp[i*2], dp[i]+1)

    if dp[i*3] == 0:
        dp[i*3] = dp[i] + 1
    else:
        dp[i*3] = min(dp[i*3],dp[i]+1)

print(dp[n])