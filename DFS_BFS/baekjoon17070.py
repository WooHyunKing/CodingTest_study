# n = int(input())

# area = [list(map(int,input().split())) for _ in range(n)]

# inital_pipe = [(0,0),(0,1)]

# answer = 0


# def check_direction(status): # 가로인지 세로인지 대각선인지 파악하는 함수
#     if abs(status[0][0] - status[1][0]) == 1 and abs(status[0][1] - status[1][1]) == 1:
#         return "diagonal"
#     elif abs(status[0][0] - status[1][0]) == 1:
#         return "vertical"
#     elif abs(status[0][1] - status[1][1]) == 1:
#         return "horizontal"
    
# def dfs(pipe):

#     global answer

#     # print(pipe)

#     # print(pipe[0][0], pipe[0][1], pipe[1][0],pipe[1][1])

#     if pipe[1][0] == n-1 and pipe[1][1] == n-1:
#         answer += 1
#         return
    
#     if check_direction(pipe) == "horizontal": # 가로인 경우
#         temp = pipe.pop(0)
#         x, y = pipe[0][0], pipe[0][1]

#         if 0 <= y+1 < n and area[x][y+1] == 0:
#             pipe.append((x,y+1))
#             dfs(pipe)
#             pipe.pop()
        
#         if 0 <= x+1 < n and 0 <= y+1 < n and area[x][y+1] == 0 and area[x+1][y] == 0 and area[x+1][y+1] == 0:
#             pipe.append((x+1,y+1))
#             dfs(pipe)
#             pipe.pop()
        
#         pipe.insert(0,temp)
#         return
    
#     elif check_direction(pipe) == "vertical": # 세로인 경우
#         temp = pipe.pop(0)
#         x, y = pipe[0][0], pipe[0][1]
#         if 0 <= x+1 < n and area[x+1][y] == 0:
#             pipe.append((x+1,y))
#             dfs(pipe)
#             pipe.pop()
        
#         if 0 <= x+1 < n and 0 <= y+1 < n and area[x][y+1] == 0 and area[x+1][y] == 0 and area[x+1][y+1] == 0:
#             pipe.append((x+1,y+1))
#             dfs(pipe)
#             pipe.pop()
#         pipe.insert(0,temp)
#         return
    
#     elif check_direction(pipe) == "diagonal":
#         temp = pipe.pop(0)
#         x, y = pipe[0][0], pipe[0][1]
#         if 0 <= x+1 < n and area[x+1][y] == 0:
#             pipe.append((x+1,y))
#             dfs(pipe)
#             pipe.pop()

#         if 0 <= y+1 < n and area[x][y+1] == 0:
#             pipe.append((x,y+1))
#             dfs(pipe)
#             pipe.pop()
        
#         if 0 <= x+1 < n and 0 <= y+1 < n and area[x][y+1] == 0 and area[x+1][y] == 0 and area[x+1][y+1] == 0:
#             pipe.append((x+1,y+1))
#             dfs(pipe)
#             pipe.pop()
#         pipe.insert(0,temp)
#         return

# if area[n-1][n-1] == 0:        
#     dfs(inital_pipe)

# print(answer)

############################################### dfs

# n = int(input())

# house = [list(map(int,input().split())) for _ in range(n)]
# visited = [[False]*n for _ in range(n)]

# dx_r, dy_r = [0,1], [1,1] # 가로일 경우 움직일 수 있는 방향
# dx_c, dy_c = [1,1], [0,1] # 세로일 경우 움직일 수 있는 방향
# dx_d, dy_d = [0,1,1], [1,0,1] # 대각선일 경우 움직일 수 있는 방향

# answer = 0

# def dfs(x,y,direction):
#     # visited[x][y] = True

#     global answer

#     if x == n-1 and y == n-1:
#         answer += 1
#         return

#     if direction == "row":

#         if 0 <= y+1 < n and house[x][y+1] == 0:
#             dfs(x,y+1,"row")
#         if 0 <= x+1 < n and 0 <= y+1 < n and house[x][y+1] == 0 and house[x+1][y] == 0 and house[x+1][y+1] == 0:
#             dfs(x+1,y+1,"dig")

#     elif direction == "col":
#         if 0 <= x+1 < n and house[x+1][y] == 0:
#             dfs(x+1,y,"col")
#         if 0 <= x+1 < n and 0 <= y+1 < n and house[x][y+1] == 0 and house[x+1][y] == 0 and house[x+1][y+1] == 0:
#             dfs(x+1,y+1,"dig")

#     elif direction == "dig":
#         if 0 <= y+1 < n and house[x][y+1] == 0:
#             dfs(x,y+1,"row")
#         if 0 <= x+1 < n and house[x+1][y] == 0:
#             dfs(x+1,y,"col")
#         if 0 <= x+1 < n and 0 <= y+1 < n and house[x][y+1] == 0 and house[x+1][y] == 0 and house[x+1][y+1] == 0:
#             dfs(x+1,y+1,"dig")   

# dfs(0,1,"row")

# print(answer)

############################################### dp

n = int(input())

# 0 : 가로, 1: 세로, 2: 대각선
dp = [[[0]*n for _ in range(n)]for _ in range(3)]

house = [list(map(int,input().split())) for _ in range(n)]

dp[0][0][1] = 1

for i in range(2,n):
    if house[0][i] == 0:
        dp[0][0][i] = dp[0][0][i-1]

for i in range(1,n):
    for j in range(1,n):
        if house[i][j] == 0 and house[i][j-1] == 0 and house[i-1][j] == 0:
            dp[2][i][j] = dp[0][i-1][j-1] + dp[1][i-1][j-1] +dp[2][i-1][j-1]

        if house[i][j] == 0:
            dp[0][i][j] = dp[0][i][j-1] + dp[2][i][j-1]

            dp[1][i][j] = dp[1][i-1][j] + dp[2][i-1][j]

print(sum([dp[i][n-1][n-1] for i in range(3)]))
