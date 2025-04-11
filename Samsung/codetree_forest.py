import sys
from collections import deque

input = sys.stdin.readline

# R x C 격자 형태의 마법의 숲
# 숲의 동/서/남은 벽으로 막혀 있으며, 숲의 북쪽을 통해서만 숲을 들어올 수 있다.

# 총 K명의 정령은 각자 골렘을 타고 숲을 탐색
# 각 골렘은 십자가 모양의 구조를 가지고 있으며, 중앙 칸을 포함해 총 5칸을 차지
# 골렘의 중앙을 제외한 4칸 중 1칸은 골렘의 출구이다.
# 정령은 어떤 방향에서든 골렘에 탑승할 수 있지만, 내릴 때는 정해진 출구로만 내릴 수 있다.

# i번째로 숲을 탐색하는 골렘은 숲의 가장 북쪽에서 시작하여 골렘의 중앙이 ci 열이 되도록하는 위치에서 내려오기 시작
# 초기 골렘의 출구는 di의 방향에 위치해 있다.

# 골렘은 숲을 탐색하기 위해 다음과 같은 우선순위로 이동한다.
# 더 이상 움직이지 못할 때까지 해당 과정을 반복한다.

# 1. 남쪽으로 1칸 내려간다.
# (밑으로 이동하려는 3칸이 비어있을 때만 남쪽으로 내려갈 수 있다.)

# 2. 1번의 방법으로 이동할 수 없다면 왼쪽으로 회전하면서 내려간다.
# (왼쪽으로 이동하려는 3칸 + 아래로 내려가려는 2칸이 비어있을 경우에만 가능)
# (이때, 출구도 왼쪽 반시계방향으로 이동)

# 3. 1,2번 방법으로 이동할 수 없다면 오른쪽으로 회전하면서 내려간다.
# (오른쪽으로 이동하려는 3칸 + 아래로 내려가려는 2칸이 비어있을 경우에만 가능)
# (이때, 출구도 오른쪽 시계방향으로 이동)

# 골렘이 가장 아래쪽에 도달하여 더 이상 내려갈 수 없다면
# 정령은 골렘 내에서 상하좌우 인접한 칸으로 이동할 수 있다.
# 단, 현재 위치하고 있는 골렘의 출구가 다른 골렘과 인접하고 있다면 해당 출구를 통해 다른 골렘으로 이동할 수 있다.

# 정령은 갈 수 있는 모든 칸 중 가장 아래 칸으로 이동하고 이동을 완전히 종료
# 이때 정령의 위치가 해당 정령의 최종 위치가 된다.

# 이 문제에서는 [정령의 최종 위치의 행 번호의 합]을 구해야 하기 때문에 [각 정령이 도달하게 되는 최종 위치]를 누적해야한다.

# 만약 골렘이 최대한 아래쪽으로 이동했지만 골렘의 몸 일부가 숲을 벗어난 상태라면, 
# 해당 골렘을 포함해서 숲에 위치한 모든 골렘들은 숲을 빠져나간 뒤 다음 골렘부터 새롭게 숲을 탐색하기 시작한다.

# 단, 이 경우에는 정령이 도달하는 최종 위치를 답에 포함시키지 않는다 !!!

# 출력 : 각 정령들이 최종적으로 위치하게 된 행의 총합
# 유의사항 : 숲이 텅 비게 되어도 행의 총합은 누적된다.

# 숲의 크기 R/C,  정령의 수 K
R, C, K = map(int,input().split())

answer = 0

command = [list(map(int,input().split())) for _ in range(K)]

dx, dy = [-1,0,1,0], [0,1,0,-1]

direction_dict = dict()

coor_dict = dict()

area = [[0]*C for _ in range(R+3)]

def bfs(x,y):

    visited = [[False]*C for _ in range(R+3)]
    
    q = deque([(x,y)])

    visited[x][y] = True

    maximum = -1

    while q:
        current_x, current_y = q.popleft()
        current_index = area[current_x][current_y]
        d = direction_dict[current_index]
        ox, oy = coor_dict[current_index]
        exit_x, exit_y = ox+dx[d], oy+dy[d]
        
        maximum = max(maximum, current_x)

        for i in range(4):
            next_x, next_y = current_x + dx[i], current_y + dy[i]

            if next_x < 0 or next_y < 0 or next_x >= R+3 or next_y >= C:
                continue

            if visited[next_x][next_y]:
                continue

            if area[next_x][next_y] == 0:
                continue

            # 같은 골렘인 경우
            if area[current_x][current_y] == area[next_x][next_y]:
                q.append((next_x,next_y))
                visited[next_x][next_y] = True
            
            # 다른 골렘인 경우
            else:
                if current_x == exit_x and current_y == exit_y:
                    q.append((next_x,next_y))
                    visited[next_x][next_y] = True
    
    return maximum
                

            


# 골렘이 출발하는 열 ci, 골렘의 출구 방향 di(상-우-하-좌)
for i, value in enumerate(command):

    ci, di = value[0], value[1]

    g_index = i + 1

    # 0 인덱스 맞추기 위해 -1
    ci -= 1

    direction_dict[g_index] = di

    # # 인덱스 저장
    # area[1][ci] = g_index

    # # 골렘 세우기
    # for index in range(4):
    #     nx, ny = 1 + dx[index], ci + dy[index]
    #     area[nx][ny] = g_index

    cx, cy = 1, ci

    # 더 이상 움직이지 못할 때까지 해당 과정을 반복
    while True:
        # 1. 남쪽으로 1칸 내려간다.
        # (밑으로 이동하려는 3칸이 비어있을 때만 남쪽으로 내려갈 수 있다.)

        if cx+2 < R+3 and area[cx+2][cy] == 0 and area[cx+1][cy-1] == 0 and area[cx+1][cy+1] == 0:
            cx += 1
            continue

        # 2. 1번의 방법으로 이동할 수 없다면 왼쪽으로 회전하면서 내려간다.
        # (왼쪽으로 이동하려는 3칸 + 아래로 내려가려는 2칸이 비어있을 경우에만 가능)
        # (이때, 출구도 왼쪽 반시계방향으로 이동)

        if cx+2 < R+3 and cy-2 >= 0 and area[cx][cy-2] == 0 and area[cx-1][cy-1] == 0 and area[cx+1][cy-1] == 0 and area[cx+2][cy-1] == 0 and area[cx+1][cy-2] == 0:
            cx += 1
            cy -= 1
            direction_dict[g_index] = (direction_dict[g_index] -1 + 4)%4
            continue

        # 3. 1,2번 방법으로 이동할 수 없다면 오른쪽으로 회전하면서 내려간다.
        # (오른쪽으로 이동하려는 3칸 + 아래로 내려가려는 2칸이 비어있을 경우에만 가능)
        # (이때, 출구도 오른쪽 시계방향으로 이동)

        if cx+2 < R+3 and cy+2 < C and area[cx][cy+2] == 0 and area[cx-1][cy+1] == 0 and area[cx+1][cy+1] == 0 and area[cx+1][cy+2] == 0 and area[cx+2][cy+1] == 0:
            cx += 1
            cy += 1
            direction_dict[g_index] = (direction_dict[g_index] +1 )%4
            continue

        break

    area[cx][cy] = g_index
    coor_dict[g_index] = (cx,cy)

    for i in range(4):
        nx, ny = cx + dx[i], cy + dy[i]
        area[nx][ny] = g_index

    # < 골렘이 숲을 벗어났는지 확인 >
    # 만약 골렘이 최대한 아래쪽으로 이동했지만 골렘의 몸 일부가 숲을 벗어난 상태라면, 
    # 해당 골렘을 포함해서 숲에 위치한 모든 골렘들은 숲을 빠져나간 뒤 다음 골렘부터 새롭게 숲을 탐색하기 시작한다.

    is_over = False

    for i in range(0,3):
        if is_over:
            break
        for j in range(C):
            if area[i][j] != 0:
                is_over = True
                break
    
    if is_over:
        area = [[0]*C for _ in range(R+3)]
        direction_dict = dict()
        coor_dict = dict()
        continue

    # < 골렘의 이동 및 행 점수 획득 >
    # 골렘이 가장 아래쪽에 도달하여 더 이상 내려갈 수 없다면
    # 정령은 골렘 내에서 상하좌우 인접한 칸으로 이동할 수 있다.
    # 단, 현재 위치하고 있는 골렘의 출구가 다른 골렘과 인접하고 있다면 해당 출구를 통해 다른 골렘으로 이동할 수 있다.
    temp_result = bfs(cx,cy)-2

    answer += temp_result

print(answer)