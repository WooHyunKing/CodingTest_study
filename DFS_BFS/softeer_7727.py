import sys

input = sys.stdin.readline

# m명의 친구를 불러 나무에서 열매를 수확
# n x n 크기의 격자에 모든 칸에 나무가 심어져있고, 각 나무마다 가능한 열매 수확량이 주어져 있음

# 친구들은 서로 다른 위치에서 출발하여 1초에 1칸씩 상하좌우로 움직임
# 최종적으로 모든 열매 수확량의 합을 최대로 만들고자 함

# 한 나무에 여러 친구가 방문하게 되더라도 열매는 딱 한번만 수확 가능
# 또한, 친구들끼리 이동하는 도중 만나는 것도 가능

# m명의 친구들이 3초동안 최대로 얻을 수 있는 열매 수확량의 총합

n, m = map(int,input().split())

area = [list(map(int,input().split())) for _ in range(n)]

start_coor = [tuple(map(int,input().split())) for _ in range(m)]
start_coor = [(x-1,y-1) for x,y in start_coor]

visited = [False]*m

dx, dy = [-1,1,0,0], [0,0,-1,1]

total = 0

answer = float("-inf")

def dfs(x,y,depth,index):

    global total
    global visited
    global answer

    visited[index] = True

    value = area[x][y]
    total += value
    area[x][y] = 0 

    if depth == 4:

        if all(visited):
            answer = max(total, answer)
        
        for i, coors in enumerate(start_coor):
            if not visited[i]:
                dfs(coors[0],coors[1],1,i)
                
        visited[index] = False
        total -= value
        area[x][y] += value
        
        return

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            dfs(nx,ny,depth+1,index)

    visited[index] = False
    total -= value
    area[x][y] += value
            
dfs(start_coor[0][0],start_coor[0][1],1,0)

print(answer)