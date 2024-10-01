# 초기에 격자의 모든 칸에는 블록이 하나씩 들어있고, 블록은 검은색 블록, 무지개 블록, 일반 블록이 있다.

# 일반 블록은 M가지 색상이 있고, 색은 M이하의 자연수로 표현
# 검은색 블록은 -1, 무지개 블록은 0으로 표현

# 블록 그룹은 연결된 블록의 집합이다. 그룹에는 일반 블록이 적어도 하나 있어야 하며, 일반 블록의 색은 모두 같아야 한다. 
# 검은색 블록은 포함되면 안 되고, 무지개 블록은 얼마나 들어있든 상관없다. 

# 그룹에 속한 블록의 개수는 2보다 크거나 같아야 하며, 임의의 한 블록에서 그룹에 속한 인접한 칸으로 이동해서 그룹에 속한 다른 모든 칸으로 이동할 수 있어야 한다.

# 블록 그룹의 기준 블록은 무지개 블록이 아닌 블록 중에서 행의 번호가 가장 작은 블록, 그러한 블록이 여러개면 열의 번호가 가장 작은 블록

# 오토 플레이는 다음과 같은 과정이 블록 그룹이 존재하는 동안 계속해서 반복

# 1. 크기가 가장 큰 블록 그룹 / 포함된 무지개 블록의 수가 가장 많은 블록 그룹 / 기준 블록의 행이 가장 큰 것 / 기준 블록의 열이 가장 큰 것
# 2. 1에서 찾은 블록 그룹의 모든 블록을 제거, 블록 그룹에 포함된 블록의 수를 B라고 했을 때, B^2점을 획득
# 3. 격자에 중력이 작용(검은색 블록을 제외한 모든 블록이 행의 번호가 큰 칸으로 이동)
# 4. 격자가 90도 반시계 방향으로 회전
# 5. 다시 격자에 중력이 작용(검은색 블록을 제외한 모든 블록이 행의 번호가 큰 칸으로 이동)

import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int,input().split()) # 한 변의 크기 N, 색상의 개수 M

area = [list(map(int,input().split())) for _ in range(N)]

score = 0

dx, dy = [-1,1,0,0], [0,0,-1,1]

def get_group(x, y): # 모든 블록 그룹을 찾는 함수(반환값 : 블록의 좌표 값들, 크기, 무지개 블록 수, 기준 블록의 행, 기준 블록의 열)

    coors = [(x,y)]
    coors_2 = [(x,y)]
    visited_2 = [[False]*N for _ in range(N)]

    count = 1
    rainbow_count = 0
    
    q = deque([(x,y)])

    color = area[x][y]
    visited[x][y] = True
    visited_2[x][y] = True

    while q:
        cx, cy = q.popleft()
        
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < N and 0 <= ny < N and not visited_2[nx][ny] and (area[nx][ny] == color or area[nx][ny] == 0):
                if area[nx][ny] == color:
                    visited[nx][ny] = True
                    coors_2.append((nx,ny))
                elif area[nx][ny] == 0:
                    rainbow_count += 1
                coors.append((nx,ny))
                q.append((nx,ny))
                visited_2[nx][ny] = True
                count += 1

    coors_2.sort(key = lambda x:(x[0], x[1]))

    if count < 2:
        return -1

    return [coors, count, rainbow_count, coors_2[0][0], coors_2[0][1]]

def step_one_and_two():

    global score

    group_list = []

    for i in range(N):
        for j in range(N):
            if area[i][j] != 0 and area[i][j] != -1 and area[i][j] != float("inf") and not visited[i][j]:
                result = get_group(i,j) # [[(0, 0), (0, 1)], 2, 0, 0, 0]
                if result == -1:
                    continue
                group_list.append(result)
    
    if not group_list:
        return False
    
    group_list.sort(key = lambda x:(-x[1],-x[2],-x[3],-x[4]))

    for x, y in group_list[0][0]:
        area[x][y] = float("inf")

    score += group_list[0][1]**2

    return True

def down(): # 중력을 작용하는 함수
    
    for i in range(N-1,-1,-1):
        for j in range(N):
            if area[i][j] != -1 and area[i][j] != float("inf"):
                cx, cy = i, j

                while True:
                    if cx == N-1 or area[cx+1][cy] != float("inf"):
                        break
                    cx += 1

                if i != cx:
                    area[cx][cy] = area[i][j]
                    area[i][j] = float("inf")

def rotate90_left(): # 반시계 방향으로 90도 회전시키는 함수

    global area
    
    new_area = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            new_area[N-j-1][i] = area[i][j]
    
    area = new_area

while True:

    visited =[[False]*N for _ in range(N)]

    if not step_one_and_two():
        break
    down()
    rotate90_left()
    down()

print(score)