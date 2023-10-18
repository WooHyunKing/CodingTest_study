from collections import deque

t = int(input())

dx = [-1,-2,-2,-1,1,2,2,1]
dy = [-2,-1,1,2,-2,-1,1,2]

for _ in range(t):

    n = int(input())

    start_x, start_y = map(int,input().split())
    dest_x, dest_y = map(int,input().split())

    visited = [[-1]*n for _ in range(n)]

    def bfs(x,y):
        
        visited[x][y] = 0
        
        queue = deque([(x,y)])

        while queue:
            
            curr_x,curr_y = queue.popleft()
            
            for i in range(8):
                nx = curr_x + dx[i]
                ny = curr_y + dy[i]

                if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[curr_x][curr_y] + 1
                    queue.append((nx,ny))
    
    bfs(start_x,start_y)

    print(visited[dest_x][dest_y])