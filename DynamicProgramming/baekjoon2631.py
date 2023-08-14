n = int(input())

data = []

dp = [1]*n

for i in range(n):
    data.append(int(input()))

for i in range(n):
    for j in range(i):
        if data[i] > data[j]:
            dp[i] = max(dp[i],dp[j]+1)

print(n - max(dp))