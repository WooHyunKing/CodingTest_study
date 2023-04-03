n, k = map(int,input().split())

price = [0] * (n+1)

for i in range(1,n+1):
    price[i] = int(input())

dp = [[0]*(k+1) for _ in range(n+1)]

for i in range(n+1):
     for j in range(k+1):
          if j == 0:
               dp[i][j]= 1 

for i in range(1,n+1):
    for j in range(1,k+1):
            if j >= price[i]:
                dp[price[i]][j] = dp[price[i]-1][j] + dp[price[i]][j-price[i]]
            else:
                 dp[price[i]][j] = dp[price[i]-1][j]
print(dp)