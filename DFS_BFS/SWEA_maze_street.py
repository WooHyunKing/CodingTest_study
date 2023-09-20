from collections import deque

t= int(input())

dx = [-1,1,0,0]
dy = [0,0,-1,1]

answer = []

for _ in range(t):

    n = int(input())

    maze = [list(map(int,list(input()))) for _ in range(n)]
    visited = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2:
                start_x, start_y = i, j

    def bfs(x,y):
        visited[x][y] = -1

        queue = deque([(x,y)])

        while queue:
            cur_x, cur_y = queue.popleft()
            
            for i in range(4):
                nx = cur_x + dx[i]
                ny = cur_y + dy[i]

                if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                    if maze[nx][ny] == 3:
                        return visited[cur_x][cur_y] + 1
                    elif maze[nx][ny] == 0:
                        visited[nx][ny] = visited[cur_x][cur_y] + 1
                        queue.append((nx,ny))

        return 0
    
    answer.append(bfs(start_x,start_y))

for i,value in enumerate(answer):
    print(f"#{i+1} {value}")