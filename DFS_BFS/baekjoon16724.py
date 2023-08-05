import sys
sys.setrecursionlimit(10**5)
n,m = map(int,input().split())

area = [list(input()) for _ in range(n)]

visited = [[False]*m for _ in range(n)]

count = 0

temp_x, temp_y = 0, 0

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y):

    if visited[x][y]:
        return False
    
    visited[x][y] = True

    if area[x][y] == "D":
        nx = x + 1
        ny = y
    elif area[x][y] == "R":
        nx = x
        ny = y + 1
    elif area[x][y] == "L":
        nx = x
        ny = y - 1
    elif area[x][y] == "U":
        nx = x - 1
        ny = y
        
    if 0 <=  nx < n and 0 <= ny < m:
        if not visited[nx][ny]:
            if dfs(nx,ny):
                return True
            else:
                visited[x][y] = False
                return False
        else:
            if temp_x == nx and temp_y == ny:
                return True
            else:
                visited[x][y] = False
                return False
    else:
        visited[x][y] = False
        return False

for i in range(n):
    for j in range(m):
        temp_x, temp_y = i,j
        if dfs(i,j):
            count += 1

print(count)