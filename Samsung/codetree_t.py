import sys

input = sys.stdin.readline

N, M, P, C, D = map(int, input().split())

rx, ry = map(int, input().split())

area = [[0]*N for _ in range(N)]

dx, dy = [-1,0,1,0], [0,1,0,-1]

santa_list = []

santa_mental = [0]*(P+1)

score = [0]*(P+1)

# (처음 산타와 루돌프의 위치는 겹쳐져 주어지지 않음)

def debug():
    for a in area:
        print(a)
    print()

def check_all_santa():
    for i in santa_list:
        if i[0] != -1:
            return True
    return False

def mental_boom():
    for i in range(len(santa_mental)):
        if santa_mental[i] > 0:
            santa_mental[i] -= 1

def score_up():
    for i in range(len(santa_list)):
        if santa_list[i][0] != -1:
            score[i+1] += 1

def cal(x1, y1, x2, y2): # 거리 계산 함수
    return (x1-x2)**2 + (y1-y2)**2

def get_santa(): # 가장 가까운 산타를 구하는 함수
    info = [] # (거리, 행 r, 열 c)
    for santa_index, sx, sy in santa_list:
        if santa_index == -1 and sx == -1 and sy == -1:
            continue
        info.append((cal(rx, ry, sx, sy), sx, sy, santa_index))
    info.sort(key=lambda x: (x[0], -x[1], -x[2]))
    if info:
        return info[0]
    else:
        return []

# < 루돌프의 움직임 >
def move_to_santa(x, y, sx, sy):
    rx, ry = x, y
    direction_x = 0
    direction_y = 0

    if rx < sx:
        rx += 1
        direction_x += 1
    elif rx > sx:
        rx -= 1
        direction_x -= 1

    if ry < sy:
        ry += 1
        direction_y += 1
    elif ry > sy:
        ry -= 1
        direction_y -= 1

    return rx, ry, direction_x, direction_y

# < 산타의 움직임 >
def move_to_rudol(x, y, rx, ry, santa_index):
    current_dis = cal(x, y, rx, ry)
    info = [] # (거리, 방향 인덱스, nx, ny, santa_index)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < N and 0 <= ny < N and (area[nx][ny] == 0 or area[nx][ny] == -1):
            dis = cal(nx, ny, rx, ry)
            if dis < current_dis:
                info.append((dis, i, nx, ny, santa_index))
    info.sort(key=lambda x: (x[0], x[1]))
    if info:
        return info[0]
    else:
        return []

def interact(x, y, dx_dir, dy_dir, si):
    temp = area[x][y]
    next_x, next_y = x + dx_dir, y + dy_dir
    area[x][y] = si
    santa_list[si-1] = (si, x, y)

    if 0 <= next_x < N and 0 <= next_y < N:
        if area[next_x][next_y] != 0 and area[next_x][next_y] != -1:
            interact(next_x, next_y, dx_dir, dy_dir, temp)
        else:
            area[next_x][next_y] = temp
            santa_list[temp-1] = (temp, next_x, next_y)
    else:
        santa_list[temp-1] = (-1, -1, -1)

# < 충돌 >
def crash_r_to_s(x, y, sx, sy, santa_index, dx, dy): # 루돌프가 움직여 충돌한 경우
    global rx
    global ry
    score[santa_index] += C
    santa_mental[santa_index] = 2

    next_x, next_y = sx + (dx * C), sy + (dy * C)
    rx, ry = x, y
    area[rx][ry] = -1

    if 0 <= next_x < N and 0 <= next_y < N:
        if area[next_x][next_y] != 0 and area[next_x][next_y] != -1:
            interact(next_x, next_y, dx, dy, santa_index)
        else:
            area[next_x][next_y] = santa_index
            santa_list[santa_index-1] = (santa_index, next_x, next_y)
    else:
        santa_list[santa_index-1] = (-1, -1, -1)

def crash_s_to_r(rx, ry, sx, sy, santa_index, dx, dy): # 산타가 움직여 충돌한 경우
    score[santa_index] += D
    santa_mental[santa_index] = 2
    # 수정된 부분: C -> D
    next_x, next_y = sx + (-dx * D), sy + (-dy * D)

    if 0 <= next_x < N and 0 <= next_y < N:
        if area[next_x][next_y] != 0 and area[next_x][next_y] != -1:
            interact(next_x, next_y, -dx, -dy, santa_index)
        else:
            area[next_x][next_y] = santa_index
            santa_list[santa_index-1] = (santa_index, next_x, next_y)
    else:
        santa_list[santa_index-1] = (-1, -1, -1)  

# 초기화
rx -= 1
ry -= 1

for _ in range(P):
    santa_i, sx, sy = map(int, input().split())
    sx -= 1
    sy -= 1
    area[sx][sy] = santa_i # 산타(인덱스)
    santa_list.append((santa_i, sx, sy))

area[rx][ry] = -1 # 루돌프(-1)

for mi in range(M):
    if not check_all_santa():
        break

    santa_info = get_santa() # (거리, sx, sy, santa_index)

    if not santa_info:
        continue

    result_1 = move_to_santa(rx, ry, santa_info[1], santa_info[2]) # (next_rx, next_ry, d1, d2)
    if result_1:
        next_rx, next_ry, d1, d2 = result_1

    area[rx][ry] = 0

    if area[next_rx][next_ry] != 0 and area[next_rx][next_ry] != -1: # 충돌한 경우
        crash_r_to_s(next_rx, next_ry, next_rx, next_ry, area[next_rx][next_ry], d1, d2)
    else: # 충돌하지 않은 경우
        area[next_rx][next_ry] = -1
        rx = next_rx
        ry = next_ry

    # 산타들의 움직임
    for si, sx, sy in list(santa_list): # list()로 복사하여 순회 중 변경 방지
        if si == -1 and sx == -1 and sy == -1:
            continue
        if santa_mental[si] > 0:
            continue
        result_2 = move_to_rudol(sx, sy, rx, ry, si)
        if not result_2:
            continue
        d, di, nx, ny, si = result_2

        area[sx][sy] = 0

        if area[nx][ny] == -1: # 충돌한 경우
            crash_s_to_r(rx, ry, nx, ny, si, dx[di], dy[di])
        else:
            area[nx][ny] = si
            santa_list[si-1] = (si, nx, ny)

    mental_boom()
    score_up()

for i in range(1, len(score)):
    print(score[i], end=' ')