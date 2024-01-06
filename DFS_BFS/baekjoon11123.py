import sys
from collections import deque
input = sys.stdin.readline

t = int(input().rstrip())
    
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for _ in range(t):

    h,w = map(int,input().split())

    answer = 0

    area = [list(input().rstrip()) for _ in range(h)]
    visited = [[False]*w for _ in range(h)]

    def bfs(x,y):

        if visited[x][y] or area[x][y] == ".":
            return False
    
        queue = deque([(x,y)])

        visited[x][y] = True

        while queue:
            temp_x, temp_y = queue.popleft()
            
            for i in range(4):
                nx = temp_x + dx[i]
                ny = temp_y + dy[i]
                
                if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and area[nx][ny] == "#":
                    visited[nx][ny] = True
                    queue.append((nx,ny))

        return True
    
    for i in range(h):
        for j in range(w):
            if bfs(i,j):
                answer += 1
    
    print(answer)