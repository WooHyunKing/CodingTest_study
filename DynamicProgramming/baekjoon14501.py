n = int(input())

data = []

for i in range(n):
    data.append(tuple(map(int,input().split())))

dp = [0] * 1006

for i in range(n-1,-1,-1):
    
    time = data[i][0]
    value = data[i][1]

    if (i+time) <= n:
        dp[i] = max(value+dp[i+time],dp[i+1])
    else:
        dp[i] = dp[i+1]

print(dp[0])