# M명의 참가자가 미로 탈출하기 게임에 참가
# 미로는 N×N 크기의 격자

# < 1. 이동 > 
# 1초마다 모든 참가자는 한 칸씩 움직입니다.
# 두 위치 (x1,y1), (x2,y2)의 최단거리는 ∣x1−x2∣+∣y1−y2∣로 정의
# 모든 참가자는 동시에 움직입니다.
# 상하좌우로 움직일 수 있으며, 벽이 없는 곳으로 이동할 수 있습니다.
# 움직인 칸은 현재 머물러 있던 칸보다 출구까지의 최단 거리가 가까워야 합니다.
# 움직일 수 있는 칸이 2개 이상이라면, 상하로 움직이는 것을 우선시합니다.
# 참가가가 움직일 수 없는 상황이라면, 움직이지 않습니다.
# 한 칸에 2명 이상의 참가자가 있을 수 있습니다.

# < 2. 회전 >
# 모든 참가자가 이동을 끝냈으면, 다음 조건에 의해 미로가 회전합니다.
# 한 명 이상의 참가자와 출구를 포함한 가장 작은 정사각형을 잡습니다.
# 가장 작은 크기를 갖는 정사각형이 2개 이상이라면, 좌상단 r 좌표가 작은 것이 우선되고, 그래도 같으면 c 좌표가 작은 것이 우선됩니다.
# 선택된 정사각형은 시계방향으로 90도 회전하며, 회전된 벽은 내구도가 1씩 깎입니다.

# K초 동안 위의 과정을 계속 반복
# 만약 K초 전에 모든 참가자가 탈출에 성공한다면, 게임이 끝납니다.

# 미로의 각 칸은 다음 3가지 중 하나의 상태
# 1) 빈칸(0) : 참가자가 이동 가능한 칸
# 2) 벽(1~9) : 참가자가 이동할 수 없는 칸, 1이상 9이하의 내구도, 회전할 때 내구도가 1씩 깎임, 0이 되면 빈칸
# 3) 출구(-1) : 참가자가 해당 칸에 도달하면, 즉시 탈출

# 출력 : 게임이 끝났을 때, 모든 참가자들의 '이동 거리의 합'과 '출구 좌표'

import sys
from collections import deque

input = sys.stdin.readline

N, M, K = map(int,input().split())

area = [list(map(int,input().split())) for _ in range(N)]

dx, dy = [-1,1,0,0], [0,0,-1,1]

person_set = set()

move_count = 0

for _ in range(M):
    x, y = map(int,input().split())
    area[x-1][y-1] += 10
    person_set.add((x-1,y-1))

ex, ey = map(int,input().split())
ex -= 1
ey -= 1

area[ex][ey] = -1

def debug():
    for a in area:
        print(a)
    print()

def calculate(x1,y1,x2,y2): # 두 좌표 간 최단 거리를 구하는 함수
    return abs(x1-x2) + abs(y1-y2)

def move():

    global area
    global person_set
    global move_count

    temp_area = [x[:] for x in area]
    
    q = deque(list(person_set))

    while q:
        px, py = q.popleft()

        move_list = []
        
        for i in range(4):
            nx = px + dx[i]
            ny = py + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if (area[nx][ny] == 0 or area[nx][ny] >= 10 or area[nx][ny] == -1) and calculate(nx,ny,ex,ey) < calculate(px,py,ex,ey):
                    if 0 <= i <= 1:
                        move_list.append((nx,ny,1))
                    else:
                        move_list.append((nx,ny,0))
        
        if len(move_list) >= 2: # 움직일 수 있는 칸이 2개 이상이라면, 상하로 움직이는 것을 우선시합니다.
            move_list = [x for x in move_list if x[2] == 1]
        
        if move_list: # 움직일 수 있는 상황

            if move_list[0][0] == ex and move_list[0][1] == ey:
                if (px,py) in person_set:
                   person_set.remove((px,py))
                move_count += area[px][py]//10
                temp_area[px][py] -= area[px][py]
                continue
                

            temp_area[move_list[0][0]][move_list[0][1]] += area[px][py]
            move_count += area[px][py]//10
            temp_area[px][py] -= area[px][py]
            if (px,py) in person_set:
                person_set.remove((px,py))
            person_set.add((move_list[0][0],move_list[0][1]))

    area = temp_area

def find_sq(sx,sy,ex,ey,length):
    for i in range(length):
        for j in range(length):
            new_sx, new_sy = sx + i, sy + j
            new_ex, new_ey = ex + i, ey + j

            for ti in range(new_sx,new_ex+1):
                for tj in range(new_sy, new_ey+1):
                    if 0 <= new_sx < N and 0 <= new_sy < N and 0<= new_ex < N and 0 <= new_ey < N and 0 <= ti < N and 0 <= tj <= N and area[ti][tj] >= 10:
                        return (new_sx, new_sy, new_ex, new_ey)
    
    return (-1, -1, -1, -1)

def rotate_90(arr,nsx,nsy,nex,ney):

    global person_set
    
    temp_arr = [[0]*len(arr) for _ in range(len(arr))]
    p_list = []
    new_p_list = []

    for i in range(len(arr)):
        for j in range(len(arr)):
            temp_arr[j][len(arr)-1-i] = arr[i][j]
            if arr[i][j] >= 10:
                p_list.append((i+nsx,j+nsy))
    
    for i in range(len(arr)):
        for j in range(len(arr)):
            if 1 <= temp_arr[i][j] <= 9:
                temp_arr[i][j] -= 1
            if temp_arr[i][j] >= 10:
                new_p_list.append((i+nsx,j+nsy))

    for px, py in p_list:
        if (px,py) in person_set:
            person_set.remove((px,py))
    for npx, npy in new_p_list:
        person_set.add((npx,npy))
    
    return temp_arr

def rotate():

    global ex
    global ey

    nsx, nsy, nex, ney = -1,-1,-1,-1
    
    for length in range(2,N+1): # 정사각형 길이 2~N
        
        start_x, start_y = ex - (length-1), ey - (length-1)

        nsx, nsy, nex, ney = find_sq(start_x,start_y,ex,ey,length)

        if nsx != -1:
            break
    
    if nsx == -1:
        return
        
    temp_sq = [[0]*(abs(nsx-nex)+1) for _ in range((abs(nsx-nex)+1))]

    for i in range(len(temp_sq)):
        for j in range(len(temp_sq)):
            temp_sq[i][j] = area[nsx+i][nsy+j]
    
    temp_sq = rotate_90(temp_sq,nsx,nsy,nex,ney)

    for i in range(len(temp_sq)):
        for j in range(len(temp_sq)):
            area[nsx+i][nsy+j] = temp_sq[i][j]

    for i in range(len(area)):
        for j in range(len(area)):
            if area[i][j] == -1:
                ex, ey = i, j

for _ in range(K):

    if not person_set:
        break

    temp_set = set()

    for i in range(len(area)):
        for j in range(len(area)):
            if area[i][j] >= 10:
                temp_set.add((i,j))
            if area[i][j] == -1:
                ex, ey = i, j

    person_set = temp_set

    move()
    rotate()

print(move_count)
print(ex+1,ey+1)