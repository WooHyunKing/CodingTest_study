import sys

from copy import deepcopy
from collections import deque

input = sys.stdin.readline

# 유적지는 5 x 5 격자형태
# 각 칸에는 다양한 유물의 조각이 배치되어 있음
# 유물 조각은 총 7가지 종류(1~7)

# Answer : [각 턴마다 획득한 유물의 가치의 총합]

# 단, 초기에 주어지는 유적지에서는 탐사 진행 이전에 발견되지 않으며
# 첫 번째 턴에서 탐사를 진행한 이후에는 항상 유물이 발견된다고 가정해도 Ok

# K : 탐사 반복 횟수
# M : 벽면에 적힌 유물 조각 개수
K, M = map(int,input().split())

area = [list(map(int,input().split())) for _ in range(5)]

numbers = list(map(int,input().split()))

dx, dy = [-1,1,0,0], [0,0,-1,1]

def rotate90(area):

    N = len(area)

    temp_area = deepcopy(area)

    for i in range(N):
        for j in range(N):
            temp_area[j][N-1-i] = area[i][j]

    return temp_area

def rotate180(area):

    N = len(area)

    temp_area = deepcopy(area)

    for i in range(N):
        for j in range(N):
            temp_area[N-1-i][N-1-j] = area[i][j]

    return temp_area

def rotate270(area):

    N = len(area)

    temp_area = deepcopy(area)

    for i in range(N):
        for j in range(N):
            temp_area[N-1-j][i] = area[i][j]

    return temp_area

rotate_list = [rotate90, rotate180, rotate270]

def getValueAndArea(area):

    new_area = deepcopy(area)

    value = 0

    visited = [[False]*5 for _ in range(5)]

    delete_list = []

    for i in range(5):
        for j in range(5):
            if visited[i][j]:
                continue

            q = deque([(i,j,new_area[i][j])])
            visited[i][j] = True

            temp_list = []
            temp_list.append((i,j))

            count = 0

            while q:
                cx, cy, n = q.popleft()
                count += 1

                for di in range(4):
                    nx, ny = cx + dx[di], cy + dy[di]
                    
                    if nx < 0 or ny < 0 or nx >= 5 or ny >= 5:
                        continue
                    if visited[nx][ny]:
                        continue
                    if new_area[nx][ny] != n:
                        continue

                    q.append((nx,ny,n))
                    visited[nx][ny] = True
                    temp_list.append((nx,ny))
                    
            if count >= 3:
                value += count
                delete_list += temp_list

    for i, j in delete_list:
        new_area[i][j] = 0

    return value, new_area

num_index = 0

# 3) 탐사 반복
# 이 문제는 1~2번 과정까지를 1턴으로 생각하며, 총 K번의 턴에 걸쳐 진행된다.

for _ in range(K):
    
    # 1) 탐사 진행
    # 유적지 내에서 3 x 3 격자를 선택하여 격자를 회전시킬 수 있다.
    # 선택된 격자는 90도 / 180도 / 270도 중 하나의 각도만큼 회전시킬 있다.
    # (단, 선택된 격자는 항상 회전을 진행해야만 한다.)

    # 가능한 회전 방법 중 [유물 1차 획득 가치]를 최대화하고
    # 그런 방법이 여러가지인 경우, [회전한 각도가 가장 작은] 방법을 선택.
    # 그런 방법도 여러가지인 경우, [회전 중심 좌표의 열이 가장 작은 구간]을,
    # 그런 열이 같을 경우에는 [회전 중심 좌표의 행이 가장 작은 구간]을 선택

    # 유물 1차 획득 가치(+) -> 각도(-) -> 중심의 열(-) -> 중심의 행(-)

    cases = []

    answer = 0

    for i in range(1, 4):
        for j in range(1, 4):

            temp33 = [[0]*3 for _ in range(3)]

            r, c = 0, 0

            for ti in range(i-1,i+2):
                for tj in range(j-1,j+2):
                    temp33[r][c] = area[ti][tj]
                    c += 1
                r += 1
                c = 0

            for ri in range(3):
                temp55 = deepcopy(area)
                rotated33 = rotate_list[ri](temp33)

                temp_r, temp_c = 0,0

                for ti in range(i-1,i+2):
                    for tj in range(j-1, j+2):
                        temp55[ti][tj] = rotated33[temp_r][temp_c]
                        temp_c += 1
                    temp_r += 1
                    temp_c = 0
                    
                temp_value, temp_area = getValueAndArea(temp55)

                if temp_value > 0:
                    cases.append((temp_value, ri, i,j, temp_area))

    # < 종료 조건 > 
    # 단, 아직 K번의 턴을 진행하지 못했지만, 탐사 과정에서 어떤 방법을 사용하더라도
    # 유물을 획득할 수 없다면 그 즉시 탐사는 종료된다.
    # 이 경우, 얻을 수 있는 유물이 존재하지 않으므로 종료되는 턴에 값 출력 X
    if len(cases) == 0:
        break

    cases.sort(key = lambda x : (x[0], -x[1], -x[3], -x[2]))

    value, next_area = cases[-1][0], cases[-1][4]

    answer += value

    area = next_area

    # 2-1) 유물 1차 획득
    # 상하좌우로 인접한 같은 종류의 유물 조각은 서로 연결되어있다.
    # 이 조각들이 3개 이상 연결된 경우, 조각이 모여 유물이 되고 사라진다.
    # (유물의 가치 = 연결된 조각의 개수)

    # 유적의 벽면에는 1~7 사이의 숫자가 M개 적혀있다.
    # 이들은 유적에서 조각이 사라졌을 때 새로 생겨나는 조각에 대한 정보를 담고 있다.

    # 조각이 사라진 위치에는 유적의 벽면에 적혀있는 순서대로 새로운 조각이 생긴다.
    # 새로운 조각은 [열 번호가 작은 순]으로 조각이 생긴다.
    # 만약 열 번호가 같다면 [행 번호가 큰 순]으로 조각이 생긴다.
    # (벽면의 숫자는 충분히 많이 적혀있어 생겨날 조각의 수가 부족한 경우는 X)
    # (단, 유적의 벽면에 써 있는 숫자를 사용한 이후에는 다시 사용할 수 없으므로,
    # 이후 부터는 남은 숫자부터 순서대로 사용한다.)

    # 열 번호(-) -> 행 번호(+)

    for j in range(5):
        for i in range(4,-1,-1):
            if area[i][j] == 0:
                area[i][j] = numbers[num_index]
                num_index += 1

    while True:
        
        # 2-2) 유물 연쇄 획득
        # 새로운 유물 조각이 생겨난 이후에도 조각들이 3개 이상 연결될 수 있다.
        # 이 경우, 앞과 같은 방식으로 조각이 모여 유물이 되고 사라진다.

        # 사라진 위치에는 또다시 새로운 조각이 생겨나며 이는 
        # 더 이상 3개 이상 연결되지 않아 유물이 될 수 없을 때까지 반복된다 !!!

        temp_v, temp_a = getValueAndArea(area)

        if temp_v <= 0 :
            break
    
        answer += temp_v

        for j in range(5):
            for i in range(4,-1,-1):
                if temp_a[i][j] == 0:
                    temp_a[i][j] = numbers[num_index]
                    num_index += 1

        area = temp_a

    print(answer, end= " ")