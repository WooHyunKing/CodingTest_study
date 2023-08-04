# from collections import deque
# import copy

# dx = [-1,1,0,0]
# dy = [0,0,-1,1]

# n, m = map(int,input().split())

# hx, hy = map(int,input().split())

# ex, ey = map(int,input().split())

# maze = [list(map(int,input().split())) for _ in range(n)]

# wall_list = []

# result = []

# for i in range(n):
#     for j in range(m):
#         if maze[i][j] == 1:
#             wall_list.append((i,j))
#             maze[i][j] = -1

# def bfs(maze, x, y):

#     data = copy.deepcopy(maze)
    
#     visited = [[False]*m for _ in range(n)]
    
#     visited[x][y] = True
    
#     queue = deque([(x,y)])

#     while queue:
#         v = queue.popleft()
#         x, y = v[0], v[1]

#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
            
#             if nx >= 0 and nx < n and ny >= 0 and ny < m and not visited[nx][ny] and maze[nx][ny] != -1:
#                 visited[nx][ny] = True
#                 data[nx][ny] =  data[x][y] + 1
#                 queue.append((nx,ny))

#     return data[ex-1][ey-1]

# # bfs(maze,0,0)

# def getBrokenMaze(maze,x,y):
#     data = copy.deepcopy(maze)
#     data[x][y] = 0
#     return data

# for wall in wall_list:
#     temp_result = bfs(getBrokenMaze(maze,wall[0],wall[1]),hx-1,hy-1)
#     if temp_result != 0:
#         result.append(temp_result)

# if len(result) == 0:
#     print(-1)
# else:
#     print(min(result))

from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

n, m = map(int,input().split())

hx, hy = map(int,input().split())

ex, ey = map(int,input().split())

maze = [list(map(int,input().split())) for _ in range(n)]

visited = [[[0]*m for _ in range(n)] for _ in range(2)]

def bfs():
    
    visited[0][hx-1][hy-1] = 0

    queue = deque([(0,hx-1,hy-1)])

    while queue:
        v = queue.popleft()
        w, x, y = v[0], v[1], v[2]

        if x == ex -1 and y == ey -1:
            return visited[w][x][y]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if maze[nx][ny] == 0 and visited[w][nx][ny] == 0:
                    queue.append((w,nx,ny))
                    visited[w][nx][ny] = visited[w][x][y] + 1
                elif maze[nx][ny] == 1 and w == 0:
                    queue.append((w+1,nx,ny))
                    visited[w+1][nx][ny] = visited[w][x][y] + 1
    return -1

print(bfs())