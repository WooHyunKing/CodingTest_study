# 5×5 크기의 판이 5개 
# 이중 일부 칸은 참가자가 들어갈 수 있고 일부 칸은 참가자가 들어갈 수 없다.
# 참가자는 주어진 판들을 시계 방향, 혹은 반시계 방향으로 자유롭게 회전할 수 있다. 

# 회전을 완료한 후 참가자는 판 5개를 쌓는다.
# 판을 쌓는 순서는 참가자가 자유롭게 정할 수 있다.

# 이렇게 판 5개를 쌓아 만들어진 5×5×5 크기의 큐브가 바로 참가자를 위한 미로

# 입구는 정육면체에서 참가자가 임의로 선택한 꼭짓점에 위치한 칸
# 출구는 입구와 면을 공유하지 않는 꼭짓점에 위치한 칸

# 참가자는 현재 위치한 칸에서 면으로 인접한 칸이 참가자가 들어갈 수 있는 칸인 경우 그 칸으로 이동할 수 있다.
# 참가자 중에서 본인이 설계한 미로를 가장 적은 이동 횟수로 탈출한 사람이 우승

# 만약 미로의 입구 혹은 출구가 막혀있거나, 입구에서 출구에 도달할 수 있는 방법이 존재하지 않을 경우에는 탈출이 불가능한 것으로 간주

# 출력 : 주어진 판에서 가장 적은 이동 횟수로 출구에 도달할 수 있게끔 미로를 만들었을 때 몇 번 이동을 해야하는지 구해보자. 

# 4 x 4 x 4 x 4 x 4

import sys
from collections import deque

input = sys.stdin.readline

area = []

answer = float("inf")

for _ in range(5):
    area.append([list(map(int,input().split())) for _ in range(5)])

def permutations(arr,k): # 순열 구하는 함수
    cases = []

    visited = [False]*(len(arr))

    def dfs(elements):
        
        if len(elements) == k:
            cases.append(elements)
            return
        
        for i in range(len(arr)):
            if not visited[i]:
                visited[i] = True
                dfs(elements + [arr[i]])
                visited[i] = False
    dfs([])

    return cases

def products(arr,k): # 중복순열 구하는 함수
    cases = []

    def dfs(elements):
        
        if len(elements) == k:
            cases.append(elements)
            return
        
        for i in range(len(arr)):
            dfs(elements + [arr[i]])
    dfs([])

    return cases

case_list =  permutations([0,1,2,3,4],5) # 판을 쌓는 순서는 참가자가 자유롭게 정할 수 있다.
product_list = products([0,1,2,3],5) # 참가자는 주어진 판들을 시계 방향, 혹은 반시계 방향으로 자유롭게 회전할 수 있다.

def rotate90(area): # 시계 방향으로 90도 회전시키는 함수
    new_area = [[0]*5 for _ in range(5)]

    for i in range(5):
        for j in range(5):
            new_area[j][5-1-i] = area[i][j]
    return new_area

def rotate180(area): # 시계 방향으로 180도 회전시키는 함수
    new_area = [[0]*5 for _ in range(5)]
    
    for i in range(5):
        for j in range(5):
            new_area[5-1-i][5-1-j] = area[i][j]
    return new_area

def rotate270(area): # 시계 방향으로 270도 회전시키는 함수
    new_area = [[0]*5 for _ in range(5)]
    
    for i in range(5):
        for j in range(5):
            new_area[5-1-j][i] = area[i][j]

    return new_area

def rotate(arr,n): # 시계방향 90도로 n번 회전시키는 함수
    if n == 0:
        return arr
    elif n == 1:
        return rotate90(arr)
    elif n == 2:
        return rotate180(arr)
    elif n == 3:
        return rotate270(arr)
    
def find_exit(coor, coors): # 시작점을 기준으로 도착지점을 찾아주는 함수

    for x,y,z in coors:
        if abs(x-coor[0]) + abs(y-coor[1]) + abs(z-coor[2]) == 12:
            return (x,y,z)
    
starts = [(0,0,0),(0,0,4),(0,4,0),(0,4,4)] # 시작 꼭지점
vertexs = [(0,0,0),(0,0,4),(0,4,0),(0,4,4),(4,0,0),(4,0,4),(4,4,0),(4,4,4)]  # 꼭지점 모음

d = [(0,-1,0),(0,1,0),(0,0,-1),(0,0,1),(-1,0,0),(1,0,0)] # 3차원 배열에서 움직일 수 있는 방향

def bfs(arr,start,end): # 입력 : 3차원 배열 arr, 시작 (x,y,z), 도착(x,y,z), 출력 : 도착지점까지 걸리는 최소 거리

    visited = [[[-1]*5 for _ in range(5)] for _ in range(5)]

    q = deque([start])

    visited[start[0]][start[1]][start[2]] = 0

    while q:
        z,x,y = q.popleft()

        if (z,x,y) == end: # 시간초과 해결 코드(백트래킹) ⭐️
            if visited[z][x][y] == 12: 
                print(12)
                exit()

            return visited[z][x][y]

        for dz, dx, dy in d:
            nz = z + dz
            nx = x + dx
            ny = y + dy

            if 0 <= nz < 5 and 0 <= nx < 5 and 0 <= ny < 5:
                if visited[nz][nx][ny] == -1 and arr[nz][nx][ny] == 1:
                    visited[nz][nx][ny] = visited[z][x][y] + 1
                    q.append((nz,nx,ny))

    if visited[end[0]][end[1]][end[2]] == -1:
        return -1
    else:
        return visited[end[0]][end[1]][end[2]]

def find(arr): # 임의로 주어진 3차원 배열에서 최단 거리를 탐색하는 함수
    global answer
    start_and_end = [] # 시작점과 도착점 모음

    for z,x,y in starts:
        if arr[z][x][y] == 0: # 시작점이 0인 경우 Pass
            continue
        e = find_exit((z,x,y),vertexs)
        if arr[e[0]][e[1]][e[2]] == 0: # 도착점이 0인 경우 Pass
            continue
        start_and_end.append(((z,x,y),e))
    
    for start, end in start_and_end: # (0, 4, 0), (4, 0, 4)
        result = bfs(arr,start,end)
        if result != -1:
            answer = min(answer,result)


for indexs in case_list:

    qube = []

    for i in indexs:
        qube.append(area[i])
    
    for p_list in product_list: 
        temp_qube = [] # 기존 배열의 값이 바뀌지 않도록 유지해야 하므로 임시 배열 선언
        for q in qube:
            temp_qube.append([x[:] for x in q])

        for i,p in enumerate(p_list):
            temp_qube[i] = rotate(qube[i],p)

        find(temp_qube)

if answer == float("inf"):
    print(-1)
else:
    print(answer)