import sys
input = sys.stdin.readline

r,c = map(int,input().split())

area = []

result = 0

for _ in range(r):
    area.append(list(input().strip()))

dx = [-1,0,1]
dy = [1,1,1]

def dfs(x,y):
    global result

    area[x][y] = 'o'

    if y == c-1:
        result += 1
        return True
    
    for k in range(3):
        nx = x + dx[k]
        ny = y + dy[k]

        if 0 <= nx < r and 0 <= ny < c: # 구역을 벗어나는지 확인
            if area[nx][ny] != 'x' and area[nx][ny] != 'o': # 지나갔던 곳이거나 건물이 있는 경우 제외
                if dfs(nx,ny):
                    return True

for i in range(r):
    dfs(i,0)

print(result)
