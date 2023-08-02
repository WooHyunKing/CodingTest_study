from collections import deque
def solution(maps):
    
    n,m = len(maps), len(maps[0]) # 행 개수, 열 개수
    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    visited = [[False]*m for _ in range(n)]
    
    queue = deque([(0,0)])
    
    visited[0][0] = True
    
    while queue:
        x,y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < m and not visited[nx][ny] and maps[nx][ny] != 0:
                queue.append((nx,ny))
                maps[nx][ny] = maps[x][y] + 1
                visited[nx][ny] = True
    
    if maps[n-1][m-1] == 1:
        return -1
    else:
        return maps[n-1][m-1]