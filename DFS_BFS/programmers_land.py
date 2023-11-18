

def solution(land):
    answer = 0
    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    n = len(land)
    m = len(land[0])

    def dfs(x,y):

        nonlocal area

        if visited[x][y] or land[x][y] == 0:
            return False
        
        area += 1
        visited[x][y] = True

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and land[nx][ny] == 1:
                dfs(nx,ny)

        return True

    # 열 별로 체크

    for j in range(m):
        visited = [[False]*m for _ in range(n)]
        area = 0
        for i in range(n):
            dfs(i,j)
        answer = max(area,answer)

    return answer