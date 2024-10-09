# 숲의 동쪽, 서쪽, 남쪽은 마법의 벽으로 막혀 있으며, 정령들은 숲의 북쪽을 통해서만 숲에 들어올 수 있습니다.

# 총 K명의 정령은 각자 골렘을 타고 숲을 탐색
# 각 골렘은 십자 모양의 구조를 가지고 있으며, 중앙 칸을 포함해 총 5칸을 차지
# 골렘의 중앙을 제외한 4칸 중 한 칸은 골렘의 출구
# 정령은 어떤 방향에서든 골렘에 탑승할 수 있지만, 골렘에서 내릴 때에는 정해진 출구를 통해서만 내릴 수 있습니다.

# i번째로 숲을 탐색하는 골렘은 숲의 가장 북쪽에서 시작해 골렘의 중앙이 ci 열이 되도록 하는 위치에서 내려오기 시작합니다. 
# 초기 골렘의 출구는 di 의 방향에 위치해 있습니다.

# < 더 이상 움직이지 못할 때까지 해당 과정을 반복 >
# 1. 남쪽으로 한 칸 내려갑니다.(초록색 칸들이 비어있을 때에만 남쪽으로 내려갈 수 있습니다.)
# 2. (1)의 방법으로 이동할 수 없으면 서쪽 방향으로 회전하면서 내려갑니다.
# 초록색 칸들이 비어있을 때에만 서쪽 방향으로 회전하면서 내려갈 수 있습니다.
# 서쪽 방향으로 한 칸 이동을 한 뒤 내려가기 때문에 골렘을 기준으로 서쪽 한 칸이 모두 비어 있어야 함에 유의
# 3. (1)과 (2)의 방법으로 이동할 수 없으면 동쪽 방향으로 회전하면서 내려갑니다.
# 4. 골렘이 이동할 수 있는 가장 남쪽에 도달해 더이상 이동할 수 없으면 정령은 골렘 내에서 상하좌우 인접한 칸으로 이동이 가능합니다. 
# 단, 만약 현재 위치하고 있는 골렘의 출구가 다른 골렘과 인접하고 있다면 해당 출구를 통해 다른 골렘으로 이동할 수 있습니다.
# 정령은 갈 수 있는 모든 칸 중 가장 남쪽의 칸으로 이동하고 이동을 완전히 종료

# 정령의 최종 위치의 행 번호의 합을 구해야 하기에 각 정령이 도달하게 되는 최종 위치를 누적해야 합니다.

# 만약 골렘이 최대한 남쪽으로 이동했지만 골렘의 몸 일부가 여전히 숲을 벗어난 상태라면, 
# 해당 골렘을 포함해 숲에 위치한 모든 골렘들은 숲을 빠져나간 뒤 다음 골렘부터 새롭게 숲의 탐색을 시작합니다. 
# 단, 이 경우에는 정령이 도달하는 최종 위치를 답에 포함시키지 않습니다.

# 출력 : 골렘들이 숲에 진입함에 따라 각 정령들이 최종적으로 위치한 행의 총합

import sys
from collections import deque

input = sys.stdin.readline

R, C, K = map(int,input().split())

area = [[0]*C for _ in range(R+3)]
isExit = [[False]*C for _ in range(R+3)]

answer = 0

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def inRange(x,y):
    return 3 <= x < R+3 and 0 <= y < C

def debug():
    for a in area:
        print(a)
    print()

def debug_exit():
    for a in isExit:
        print(a)
    print()

def canGoDown(x,y):
    if 0 <= x+2 < R+3 and 0 <= y-1 < C and 0 <= y+1 < C:
        if area[x+2][y] == 0 and area[x+1][y-1] == 0 and area[x+1][y+1] == 0:
            return True
    return False

def canGoLeft(x,y):
    if 0 <= x+2 < R+3 and 0 <= y-2 < C:
        if area[x-1][y-1] == 0 and area[x][y-2] == 0 and area[x+1][y-1] == 0 and area[x+1][y-2] == 0 and area[x+2][y-1] == 0:
            return True
    return False

def canGoRight(x,y):
    if 0 <= x+2 < R+3 and 0 <= y+2 < C:
        if area[x-1][y+1] == 0 and area[x][y+2] == 0 and area[x+1][y+1] == 0 and area[x+1][y+2] == 0 and area[x+2][y+1] == 0:
            return True
    return False

def move(x,y,d,index):

    if canGoDown(x,y):
        return move(x+1,y,d,index)
    elif canGoLeft(x,y):
        return move(x+1,y-1,(d+3)%4,index)
    elif canGoRight(x,y):
        return move(x+1,y+1,(d+1)%4,index)
    else:
        area[x][y] = index
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            area[nx][ny] = index
        isExit[x + dx[d]][y + dy[d]] = True
        return x, y

def bfs(x,y):

    q = deque([(x,y)])
    visited = [[False]*C for _ in range(R+3)]
    visited[x][y] = True

    maximum_row = -1

    while q:
        cx, cy = q.popleft()
        maximum_row = max(maximum_row, cx)
        
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]

            if 0 <= nx < R+3 and 0 <= ny < C and not visited[nx][ny]:
                if area[cx][cy] != 0 and area[cx][cy] == area[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx,ny))
                else:
                    if area[cx][cy] != 0 and area[nx][ny] != 0 and isExit[cx][cy]:
                        visited[nx][ny] = True
                        q.append((nx,ny))
    return maximum_row-2

for index in range(1,K+1):
    c, d = map(int,input().split())
    tx, ty = move(1,c-1,d,index)

    if not inRange(tx-1,ty) or not inRange(tx,ty) or not inRange(tx,ty-1) or not inRange(tx,ty+1) or not inRange(tx+1,ty):
        area = [[0]*C for _ in range(R+3)]
        isExit = [[False]*C for _ in range(R+3)]
        continue

    answer += bfs(tx,ty)

print(answer)