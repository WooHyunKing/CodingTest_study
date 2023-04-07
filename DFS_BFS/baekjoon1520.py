import sys
sys.setrecursionlimit(50000000);

m, n = map(int,input().split())

area = [[] for _ in range(m)]
visited = [[False]*n for _ in range(m)]

count = 0

for i in range(m):
    area[i] = list(map(int,input().split()))

def dfs(x,y):

    global count
    global visited

    if visited[x][y]:
        return False
    
    if x == (m-1) and y == (n-1):
        count += 1
    
    visited[x][y] = True

    nx = [-1,1,0]
    ny = [0,0,1]

    for i in range(3):
        temp_x = x + nx[i]
        temp_y = y + ny[i]

        if temp_x >= 0 and temp_x < m and temp_y >= 0 and temp_y < n:
            if area[temp_x][temp_y] < area[x][y]:
                dfs(temp_x,temp_y)

    visited[x][y] = False

dfs(0,0)

print(count)