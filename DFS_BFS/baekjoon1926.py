from collections import deque

n, m = map(int,input().split())

area = [list(map(int,input().split())) for _ in range(n)]

visited = [[0]*m for _ in range(n)]

count_list = []

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    if visited[x][y] != 0 or area[x][y] != 1:
        return -1
    
    visited[x][y] = 1
    
    queue = deque([(x,y)])
    total = 1

    while queue:
        cur_x, cur_y = queue.popleft()

        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and area[nx][ny] == 1 and visited[nx][ny] == 0:
                visited[nx][ny] = visited[cur_x][cur_y] + 1
                total += 1
                queue.append((nx,ny))

    return total

for i in range(n):
    for j in range(m):
        count = bfs(i,j)
        if count != -1:
            count_list.append(count)

print(len(count_list))

if len(count_list) == 0:
    print(0)
else:
    print(max(count_list))