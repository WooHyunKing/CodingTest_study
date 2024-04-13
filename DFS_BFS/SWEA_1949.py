t = int(input())

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for index in range(t):

    n, k = map(int,input().split())

    area = [list(map(int,input().split())) for _ in range(n)]
    visited = [[False]*n for _ in range(n)]

    maximum_value = max(map(max,area))

    maximum_set = set()

    answer = -1

    for i, row in enumerate(area):
        for j, value in enumerate(row):
            if value == maximum_value:
                maximum_set.add((i,j))

    def dfs(x,y,depth,available):

        global answer

        visited[x][y] = True
        
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if area[nx][ny] < area[x][y]:
                    dfs(nx,ny,depth+1,available)
                else:
                    if available and abs(area[nx][ny] - area[x][y]) < k:
                        diff = abs(area[nx][ny] - area[x][y])+1
                        area[nx][ny] -= diff
                        dfs(nx,ny,depth+1, False)
                        area[nx][ny] += diff

        answer = max(answer,depth)

        visited[x][y] = False

    for mx,my in maximum_set:
        dfs(mx,my,1,True)
    
    print(f"#{index+1} {answer}")