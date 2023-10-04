n, m = map(int,input().split())

area = [list(map(int,input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

answer = -1
max_value = max(map(max,area))


def dfs(x,y,movement,value):

    global answer

    print(x,y,movement,value)

    if answer >= value + area[x][y] + max_value*(4-movement):
        return

    if movement == 4:
        answer = max(answer,value+area[x][y])
        return
    
    visited[x][y] = True

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            dfs(nx,ny,movement+1,value + area[x][y])
            
    # visited[x][y] = False

def other(x,y):
    global answer

    if 0 <= x-1 < n and 0 <= x+1 < n and 0 <= y+1 < m:
        answer = max(answer, area[x-1][y]+area[x][y]+area[x+1][y]+area[x][y+1])
    if 0 <= x+1 < n and 0 <= y-1 < m and 0 <= y+1 < m:
        answer = max(answer, area[x][y-1]+area[x][y]+area[x][y+1]+area[x+1][y])
    if 0 <= x-1 < n and 0 <= y-1 < m and 0 <= y+1 < m:
        answer = max(answer, area[x][y-1]+area[x][y]+area[x][y+1]+area[x-1][y])
    if 0 <= x-1 < n and 0 <= x+1 < n and 0 <= y-1 < m:
        answer = max(answer, area[x-1][y]+area[x][y]+area[x+1][y]+area[x][y-1])

for i in range(n):
    for j in range(m):
        dfs(i,j,1,0)
        other(i,j)

print(answer)