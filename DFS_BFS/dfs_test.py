area = [[1,2],[4,5]]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

visited = [[False]*2 for _ in range(2)]

def dfs(x,y,path):
    
    visited[x][y] = True
    print(x,y,path)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < 2 and 0 <= ny < 2 and not visited[nx][ny]:
            dfs(nx,ny,path+[(nx,ny)])
    # visited[x][y] = False
dfs(0,0,[(0,0)])

    