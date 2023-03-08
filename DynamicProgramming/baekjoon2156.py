n = int(input())

weight = [0]*10000
dp = [0]*10000

for i in range(n):
    weight[i] = int(input())

dp[0] = weight[0]
dp[1] = weight[0] + weight[1]
dp[2] = max(weight[2]+weight[0], weight[2]+weight[1], dp[1])

for i in range(3,n):
    dp[i]=max(weight[i]+dp[i-2], weight[i]+weight[i-1]+dp[i-3],dp[i-1])

print(max(dp))