from collections import deque

n,m = map(int,input().split())

maze = [list(map(int,list(input()))) for _ in range(n)]
visited = [[-1]*m for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
    visited[0][0] = 1

    queue = deque([(0,0)])

    while queue:
        cur_x,cur_y = queue.popleft()

        if cur_x == n-1 and cur_y == m-1:
            return visited[cur_x][cur_y]

        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1 and maze[nx][ny] == 1:
                visited[nx][ny] = visited[cur_x][cur_y] + 1
                queue.append((nx,ny))
    return -1

print(bfs())