# import sys
# sys.setrecursionlimit(10**6)

# n = int(input())

# dp = [0]*1000001

# def solution(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 2
#     if dp[n]:
#         return dp[n]
#     dp[n] = solution(n-2) + solution(n-1)
#     return dp[n]%15746

# print(solution(n))

n = int(input())

dp = [0]*1000001

dp[0] = 1
dp[1] = 2

for i in range(2, n):
    dp[i] = (dp[i-1] + dp[i-2])%15746

print(dp[n-1])
