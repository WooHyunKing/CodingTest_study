import sys
from collections import deque
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

# L : 육지, W : 바다

max_value = float("-inf")

n, m = map(int,input().split())

area = [list(input().rstrip()) for _ in range(n)]

def bfs(x,y):

    global max_value

    visited = [[-1]*m for _ in range(n)]
    
    visited[x][y] = 0
    
    queue = deque([(x,y)])

    while queue:
        curr_x, curr_y = queue.popleft()

        max_value = max(max_value,visited[curr_x][curr_y])

        for i in range(4):
            nx = curr_x + dx[i]
            ny = curr_y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1 and area[nx][ny] == "L":
                visited[nx][ny] = visited[curr_x][curr_y] + 1
                queue.append((nx,ny))

for i in range(n):
    for j in range(m):
        if area[i][j]=="L":
            bfs(i,j)

print(max_value)