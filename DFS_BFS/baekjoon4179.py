from collections import deque
r,c = map(int,input().split())


maze = [list(input()) for _ in range(r)]
visited = [[-1]*c for _ in range(r)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

fire_list = []

for i in range(r):
    for j in range(c):
        if maze[i][j] == "J":
            start_x, start_y = i, j
        if maze[i][j] == "F":
            fire_list.append((i,j,"F"))

def bfs():
    visited[start_x][start_y] = 0

    for fire_x,fire_y,v in fire_list:
        visited[fire_x][fire_y] = 0
    
    queue = deque(fire_list+[(start_x,start_y,"J")])

    while queue:
        cur_x, cur_y, value = queue.popleft()

        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]

            if (nx < 0 or nx >= r or ny < 0 or ny >= c) and value == "J":
                return visited[cur_x][cur_y] + 1
            
            if 0 <= nx < r and 0 <= ny < c and maze[nx][ny] == "." and visited[nx][ny] == -1:
                visited[nx][ny] = visited[cur_x][cur_y] + 1
                queue.append((nx,ny,value))

    return -1

result = bfs()

if result == -1:
    print("IMPOSSIBLE")
else:
    print(result)