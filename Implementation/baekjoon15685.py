n = int(input())

area = [[0]*101 for _ in range(101)]

data = [list(map(int,input().split())) for _ in range(n)]

answer = 0

dx = [1,0,-1,0]
dy = [0,-1,0,1]

for x,y,d,g in data:

    routes = [d]
    area[x][y] = 1

    for i in range(g):
        for j in range(len(routes)-1,-1,-1):
            routes.append((routes[j]+1)%4)

    for route in routes:
        nx, ny = x + dx[route], y + dy[route]
        area[nx][ny] = 1
        x, y = nx, ny

for i in range(100):
    for j in range(100):
        if area[i][j] == 1 and area[i][j+1] == 1 and area[i+1][j] == 1 and area[i+1][j+1] == 1:
            answer += 1

print(answer)