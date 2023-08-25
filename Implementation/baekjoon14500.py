n, m = map(int,input().split())

area = [list(map(int,input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

max_value = -1

def dfs(x,y,movement,value):

    global max_value
    
    visited[x][y] = True

    if movement == 4:
        max_value = max(max_value,value+area[x][y])
        visited[x][y] = False
        return
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            dfs(nx,ny,movement+1,value + area[x][y])
            
    visited[x][y] = False

def other(x,y):
    global max_value

    if 0 <= x-1 < n and 0 <= x+1 < n and 0 <= y+1 < m:
        max_value = max(max_value, area[x-1][y]+area[x][y]+area[x+1][y]+area[x][y+1])
    if 0 <= x+1 < n and 0 <= y-1 < m and 0 <= y+1 < m:
        max_value = max(max_value, area[x][y-1]+area[x][y]+area[x][y+1]+area[x+1][y])
    if 0 <= x-1 < n and 0 <= y-1 < m and 0 <= y+1 < m:
        max_value = max(max_value, area[x][y-1]+area[x][y]+area[x][y+1]+area[x-1][y])
    if 0 <= x-1 < n and 0 <= x+1 < n and 0 <= y-1 < m:
        max_value = max(max_value, area[x-1][y]+area[x][y]+area[x+1][y]+area[x][y-1])

for i in range(n):
    for j in range(m):
        dfs(i,j,1,0)
        other(i,j)

print(max_value)