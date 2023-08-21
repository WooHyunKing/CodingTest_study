import sys
sys.setrecursionlimit(10**5)
n,m = map(int,input().split())

area = [list(sys.stdin.readline().rstrip()) for _ in range(n)]

visited = [[-1]*m for _ in range(n)]

count = 0

index = 0

def dfs(x,y,idx):

    global count

    if visited[x][y] != -1:
        if visited[x][y] == idx:
            count += 1
        return
    
    visited[x][y] = idx

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

    dfs(nx,ny,idx)

for i in range(n):
    for j in range(m):
        dfs(i,j,index)
        index += 1
for i in visited:
    print(i)
print(count)