import sys
import copy
from collections import deque

input = sys.stdin.readline

# 유물 조각은 총 7가지 종류로, 각각 숫자 1부터 7로 표현

# 1. 탐사 진행
# 3x3 격자 선택 후 시계 방향으로 90도, 180도, 270도 중 하나의 각도만큼 회전

# (1) 유물 1차 획득 가치를 최대화하고, 그러한 방법이 여러가지인 경우 
# (2) 회전한 각도가 가장 작은 방법을 선택
# (3) 회전 중심 좌표의 열이 가장 작은 구간을, 그리고 열이 같다면 행이 가장 작은 구간을 선택
# 획득 가치(+) > 회전 각도(-) > 회전 중심의 열(-) > 회전 중심의 행(-)

# 2. 유물 획득
# 상하좌우로 인접한 같은 종류의 유물 조각은 서로 연결
# 조각들이 3개 이상 연결된 경우, 조각이 모여 유물이 되고 사라집니다. 
# (유물의 가치 = 모인 조각의 개수)

# 3. 유적의 벽면(새로운 조각 채우기)
# 유적의 벽면에는 1부터 7 사이의 숫자가 M개 적혀 있습니다. 
# 이들은 유적에서 조각이 사라졌을 때 새로 생겨나는 조각에 대한 정보를 담고 있습니다.
# 조각이 사라진 위치에는 유적의 벽면에 적혀있는 순서대로 새로운 조각이 생겨납니다
# (1) 열 번호가 작은 순
# (2) 행 번호가 큰 순으로 조각이 생겨납니다.
# 열(-) > 행(+)

# 단, 유적의 벽면에 써 있는 숫자를 사용한 이후에는 다시 사용할 수 없으므로 이후 부터는 남은 숫자부터 순서대로 사용

# 4. 유물 연쇄 획득
# 더 이상 조각이 3개 이상 연결되지 않아 유물이 될 수 없을 때까지 반복

# 5. 반복
# 탐사 진행 ~ 유물 연쇄 획득의 과정까지를 1턴으로 생각
# 총 K번의 턴에 걸쳐 진행

# 출력 : 각 턴마다 획득한 유물의 가치의 총합
# 단, 아직 K번의 턴을 진행하지 못했지만 탐사 진행 과정에서 어떠한 방법을 사용하더라도 유물을 획득할 수 없었다면 모든 탐사는 그 즉시 종료

K, M = map(int,input().split())

area = [list(map(int,input().split())) for _ in range(5)]

numbers = list(map(int,input().split()))

num_index = 0

dx, dy = [-1,1,0,0],[0,0,-1,1]

n_list = [90,180,270]

# 단, 초기에 주어지는 유적지에서는 탐사 진행 이전에 유물이 발견되지 않으며, 
# 첫 번째 턴에서 탐사를 진행한 이후에는 항상 유물이 발견됨을 가정해도 좋습니다.

# 1) 유물 획득 가치를 구하는 함수
def get_value(area):

    total = 0
    coors = []
    
    visited = [[False]*5 for _ in range(5)]

    for i in range(5):
        for j in range(5):
            if not visited[i][j]:
                q = deque([(i,j)])
                visited[i][j] = True
                value = area[i][j]
                count = 1
                temp_coors = [(i,j)]
                
                while q:
                    cx, cy = q.popleft()
                    
                    for k in range(4):
                        nx = cx + dx[k]
                        ny = cy + dy[k]
                        if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny] and area[nx][ny] == value:
                            visited[nx][ny] = True
                            count += 1
                            q.append((nx,ny))
                            temp_coors.append((nx,ny))
                if count >= 3:
                    total += count
                    coors += temp_coors
    
    return total, coors

# 2) 90도 / 180도 / 270도 회전 함수
def rotate(arr,x,y,n):

    new = copy.deepcopy(arr)
    temp_arr = [[0]*3 for _ in range(3)]
    new_arr = [[0]*3 for _ in range(3)]

    start_x, start_y = x-1,y-1

    for i in range(3):
        for j in range(3):
            temp_arr[i][j] = arr[start_x+i][start_y+j]
    if n == 90:
        for i in range(3):
            for j in range(3):
                new_arr[j][3-1-i] = temp_arr[i][j]
    elif n == 180:
        for i in range(3):
            for j in range(3):
                new_arr[3-1-i][3-1-j] = temp_arr[i][j]
    elif n == 270:
        for i in range(3):
            for j in range(3):
                new_arr[3-1-j][i] = temp_arr[i][j]
    for i in range(3):
        for j in range(3):
            new[start_x+i][start_y+j] = new_arr[i][j]

    return new

# 3) 유물 획득 가치와 정보를 구하는 함수(입력 : 중앙 x, y 좌표, 출력 : 가치, 각도, y, x)
def get_info():

    cases = []
    
    for x in range(1,4):
        for y in range(1,4):
            for n in n_list:
                new_area = rotate(area,x,y,n)
                total_value, coor_list = get_value(new_area)
                cases.append([ total_value ,n,y,x,coor_list,new_area ])
    
    cases.sort(key = lambda x:(-x[0],x[1],x[2],x[3]))

    if not cases:
        return []
    else:
        return cases[0]

# 4) 유물 조각을 채우는 함수
def add(coors):

    global num_index
    
    for x, y in coors:
        area[x][y] = numbers[num_index]
        num_index = (num_index+1)%M

for _ in range(K):

    answer = 0
    info = get_info() # [7, 90, 2, 2, [(0, 1), (1, 1), (1, 0), (2, 0), (0, 2), (1, 2), (1, 3)]]

    if info[0] < 3:
        break

    answer += info[0]

    area = info[5]

    sorted_coor = sorted(info[4],key=lambda x:(x[1],-x[0]))

    add(sorted_coor)

    while True:

        temp_total_value, temp_coor_list = get_value(area)

        if temp_total_value < 3:
            break

        answer += temp_total_value

        temp_sorted_coor = sorted(temp_coor_list,key=lambda x:(x[1],-x[0]))

        add(temp_sorted_coor)

    print(answer,end=' ')