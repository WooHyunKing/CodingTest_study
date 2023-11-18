from collections import deque

def solution(land):
    answer = 0
    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    n = len(land)
    m = len(land[0])
    
    visited = [[False]*m for _ in range(n)]
    total = [0]*m
    
    def bfs(x,y):
        
        if visited[x][y]:
            return
        
        visited[x][y] = True
        
        y_list = set()
        count = 0
        
        queue = deque([(x,y)])
        
        while queue:
            temp_x,temp_y = queue.popleft()
            count += 1
            y_list.add(temp_y)
            
            for i in range(4):
                nx = temp_x + dx[i]
                ny = temp_y + dy[i]
                
                if 0 <= nx < n and 0 <= ny < m and land[nx][ny] == 1 and not visited[nx][ny]:
                    queue.append((nx,ny))
                    visited[nx][ny] = True

        for i in y_list:
            total[i] += count
            
    
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and land[i][j] == 1:
                bfs(i,j)

    return max(total)