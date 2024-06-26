import sys

input = sys.stdin.readline

n = int(input())

dp_max = [0]*3
dp_min = [0]*3

for _ in range(n):

    a, b, c = map(int,input().split())

    temp_max = dp_max[:]
    temp_min = dp_min[:]

    for i in range(3):
        if i == 0:
            dp_max[i] = a + max(temp_max[0],temp_max[1])
            dp_min[i] = a + min(temp_min[0],temp_min[1])
        elif i == 1:
            dp_max[i] = b + max(temp_max[0],temp_max[1],temp_max[2])
            dp_min[i] = b + min(temp_min[0],temp_min[1],temp_min[2])
        elif i == 2:
            dp_max[i] = c + max(temp_max[1],temp_max[2])
            dp_min[i] = c + min(temp_min[1],temp_min[2])

print(max(dp_max),min(dp_min))
# 메모리 초과 코드
# scores = [list(map(int,input().split())) for _ in range(n)]

# dp = [[0]*3 for _ in range(n)]
# dp_2 = [[float("inf")]*3 for _ in range(n)]

# dp[0][0], dp[0][1], dp[0][2] = scores[0][0], scores[0][1], scores[0][2]
# dp_2[0][0], dp_2[0][1], dp_2[0][2] = scores[0][0], scores[0][1], scores[0][2]

# for i in range(1,n):
#     for j in range(3):
#         if j == 0:
#             dp[i][j] = max(dp[i-1][0], dp[i-1][1]) + scores[i][j]
#             dp_2[i][j] = min(dp_2[i-1][0], dp_2[i-1][1]) + scores[i][j]
#         elif j == 1:
#             dp[i][j] = max(dp[i-1][0], dp[i-1][1], dp[i-1][2]) + scores[i][j]
#             dp_2[i][j] = min(dp_2[i-1][0], dp_2[i-1][1], dp_2[i-1][2]) + scores[i][j]
#         elif j == 2:
#             dp[i][j] = max(dp[i-1][1], dp[i-1][2]) + scores[i][j]
#             dp_2[i][j] = min(dp_2[i-1][1], dp_2[i-1][2]) + scores[i][j]

# print(f"{max(dp[-1])} {min(dp_2[-1])}")