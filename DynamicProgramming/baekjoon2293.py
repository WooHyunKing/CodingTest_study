n, k = map(int,input().split())

# 1차원 DP 테이블을 사용한 풀이
prices = [0] * n

for i in range(n):
    prices[i] = int(input())

# dp[i] -> i원을 만들 때 가능한 경우의 수
dp = [0 for _ in range(k+1)]
# dp[0] -> 0원을 만들 때 가능한 경우의 수, 동전을 사용하지 않는 경우 이므로 1로 초기화
dp[0] = 1

for price in prices:
    for i in range(price,k+1):
        dp[i] = dp[i] + dp[i-price]
        
print(dp[k])

# 2차원 DP 테이블를 사용한 풀이(시간초과)

# prices = [0] * (n+1)

# for i in range(1,n+1):
#     prices[i] = int(input())

# dp = [[0]*(k+1) for _ in range(n+1)]

# for i in range(1,n+1):
#     for j in range(k+1):
#         if j==0:
#             dp[i][j] = 1

# for i in range(1,n+1):
#     for j in range(1,k+1):
#         if prices[i] > j :
#             dp[i][j] = dp[i-1][j]
#         else:
#             dp[i][j] = dp[i-1][j] + dp[i][j-prices[i]]

# print(dp[n][k])