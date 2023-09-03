t = int(input())

answer = []

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(maze,x,y,visited):
    
    if maze[x][y] == 3:
        return True
    
    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and maze[nx][ny]!=1:
            if dfs(maze,nx,ny,visited):
                return True
    
    return False
    

for _ in range(t):
    n = int(input())

    maze = [list(map(int,list(input()))) for _ in range(n)]
    visited = [[False]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2:
                start_x, start_y = i, j

    if dfs(maze,start_x,start_y,visited):
        answer.append(1)
    else:
        answer.append(0)

for i,value in enumerate(answer):
    print(f"#{i+1} {value}")