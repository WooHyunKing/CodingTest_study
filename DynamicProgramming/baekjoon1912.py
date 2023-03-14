n = int(input())

array = list(map(int,input().split()))

if n == 1:
    print(array[0])

else:
    dp = [0]*n

    dp[0] = array[0]

    for i in range(1,n):
        dp[i] = max(array[i],dp[i-1] + array[i])

    print(max(dp))