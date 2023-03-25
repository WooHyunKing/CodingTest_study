n = int(input())

data = []
dp = [1]*n

for _ in range(n):
    data.append(list(map(int,input().split())))

data.sort(key=lambda x:x[0])

for i in range(1,n):
    for j in range(i):
        if data[i][1] > data[j][1]:
            dp[i] = max(dp[i], dp[j]+1)

print(n-max(dp))