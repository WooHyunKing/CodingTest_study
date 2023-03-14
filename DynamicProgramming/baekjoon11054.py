n = int(input())

array = list(map(int,input().split()))

dp = [1]*n
dp2 = [1]*n

for i in range(n):
    for j in range(i):
        if array[i] > array[j]:
            dp[i] = max(dp[i],dp[j]+1)

for i in range(n-1,-1,-1):
    for j in range(n-1,i,-1):
        if array[i] > array[j]:
            dp2[i] = max(dp2[i],dp2[j]+1)

dp3 = [dp[i] + dp2[i] for i in range(n)]
print(max(dp3)-1)
