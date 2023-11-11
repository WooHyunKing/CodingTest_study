from collections import deque

def solution(n, m, hole):
    answer = 0
    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    area = [[0]*n for _ in range(m)]
    visited = [[[-1]*n for _ in range(m)] for _ in range(2)]
    
    for hx, hy in hole:
        area[hy-1][hx-1] = -1
    
    area[0][0],area[m-1][n-1] = 1, 2
    
    def bfs():
        visited[0][0][0] = 0
        
        queue = deque([(0,0,0)])
        
        while queue:
            w, x, y = queue.popleft()
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                nx_2 = x + dx[i]*2
                ny_2 = y + dy[i]*2
                
                if 0 <= nx < m and 0 <= ny < n:
                    # 함정이 아니고, 아직 방문하지 않은 경우
                    if area[nx][ny] != -1 and visited[w][nx][ny] == -1:
                        visited[w][nx][ny] = visited[w][x][y] + 1
                        queue.append((w,nx,ny))
                    # 다음 칸은 함정이지만 다다음칸은 함정이 아닌 경우
                    elif w == 0 and 0 <= nx_2 < m and 0 <= ny_2 < n and area[nx_2][ny_2] != -1 and visited[1][nx_2][ny_2] == -1:
                        visited[1][nx_2][ny_2] = visited[w][x][y] + 1
                        queue.append((1,nx_2,ny_2))
    bfs()
                     
    if visited[0][m-1][n-1] == -1 and visited[1][m-1][n-1] == -1:
        return -1
    elif visited[0][m-1][n-1] != -1 and visited[1][m-1][n-1] != -1:
        return min(visited[0][m-1][n-1], visited[1][m-1][n-1])
    else:
        return max(visited[0][m-1][n-1], visited[1][m-1][n-1])