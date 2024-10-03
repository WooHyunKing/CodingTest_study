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

def get_group(x, y): # 해당 좌표의 블록 그룹의 정보를 반환하는 함수(반환 값 : 블록의 좌표 값들, 블록 그룹의 크기, 무지개 블록 수, 기준 블록의 행, 기준 블록의 열)

    coors = [(x,y)] # 블록 그룹의 모든 블록을 저장하는 배열
    coors_2 = [(x,y)] # 무지개 블록이 아닌 블록만 저장하는 배열(블록 그룹의 기준 블록은 무지개 블록이 아닌 블록)
    visited_2 = [[False]*N for _ in range(N)] # 임시 방문처리 확인 배열

    count = 1 # 블록 그룹의 개수(크기)
    rainbow_count = 0 # 무지개 블록의 개수
    
    q = deque([(x,y)])

    color = area[x][y] # 초기 블록의 색깔(일반 블록의 색은 모두 같아야 함)
    visited[x][y] = True
    visited_2[x][y] = True

    while q: # BFS 알고리즘
        cx, cy = q.popleft()
        
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < N and 0 <= ny < N and not visited_2[nx][ny] and (area[nx][ny] == color or area[nx][ny] == 0):
                if area[nx][ny] == color: # 일반 블록인 경우
                    visited[nx][ny] = True # 블록 방문 처리(중복 탐색 방지)
                    coors_2.append((nx,ny)) # 무지개 블록이 아닌 블록
                elif area[nx][ny] == 0: # 무지개 블록인 경우
                    rainbow_count += 1

                coors.append((nx,ny))
                q.append((nx,ny))
                visited_2[nx][ny] = True
                count += 1
    
    # 블록 그룹의 기준 블록은 무지개 블록이 아닌 블록 중에서 행의 번호가 가장 작은 블록, 그러한 블록이 여러개면 열의 번호가 가장 작은 블록
    coors_2.sort(key = lambda x:(x[0], x[1]))

    if count < 2: # 그룹에 속한 블록의 개수는 2보다 크거나 같아야 함
        return -1

    # 반환 값 : 블록의 좌표 값들, 블록 그룹의 크기, 무지개 블록 수, 기준 블록의 행, 기준 블록의 열
    return [coors, count, rainbow_count, coors_2[0][0], coors_2[0][1]] 

def step_one_and_two(): # 오토 플레이 과정 1, 2번을 수행하는 함수

    global score

    group_list = [] # 모든 블록 그룹을 저장하는 배열

    for i in range(N):
        for j in range(N):
            if area[i][j] != 0 and area[i][j] != -1 and area[i][j] != float("inf") and not visited[i][j]:
                result = get_group(i,j) # ex) [[(0, 0), (0, 1)], 2, 0, 0, 0]
                if result == -1: # 블록의 개수가 2보다 작은 경우에는 그룹으로 취급 X
                    continue
                group_list.append(result)
    
    if not group_list: # 블록 그룹이 존재하지 않는 경우에는 False를 반환하여 while문 종료
        return False
    
    group_list.sort(key = lambda x:(-x[1],-x[2],-x[3],-x[4])) # 1) 블록 그룹 크기, 무지개 블록 수, 기준 블록 행, 기준 블록 열 기준으로 정렬

    for x, y in group_list[0][0]: # 2-1) 1에서 찾은 블록 그룹의 모든 블록을 제거
        area[x][y] = float("inf")

    score += group_list[0][1]**2 # 2-2) 블록 그룹에 포함된 블록의 수를 B라고 했을 때, B^2점을 획득

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

    if not step_one_and_two(): # 1, 2번 과정
        break # 그룹 블록이 존재하지 않을 경우 반복문 종료
    down() # 3번 과정
    rotate90_left() # 4번 과정
    down() # 5번 과정

print(score)