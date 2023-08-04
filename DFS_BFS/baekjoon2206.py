from collections import deque

n, m = map(int,input().split())

maze = [list(map(int,list(input()))) for _ in range(n)]

visited = [[[0]*m for _ in range(n)] for _ in range(2)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
    
    visited[0][0][0] = 1
    
    queue = deque([(0,0,0)])

    while queue:
        w,x,y = queue.popleft()

        if x == n-1 and y == m-1:
            return visited[w][x][y]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                if maze[nx][ny] == 0 and visited[w][nx][ny] == 0:
                    queue.append((w,nx,ny))
                    visited[w][nx][ny] = visited[w][x][y] + 1
                elif maze[nx][ny] == 1 and w == 0:
                    queue.append((w+1,nx,ny))
                    visited[w+1][nx][ny] = visited[w][x][y] + 1
    return -1

print(bfs())