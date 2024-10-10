# 루돌프는 산타들을 박치기하여 산타의 선물 배달을 방해하려고 합니다.
# 산타들은 루돌프를 잡아서 크리스마스를 구해야 합니다!

# 게임은 총 M 개의 턴에 걸쳐 진행되며 매 턴마다 루돌프와 산타들이 한 번씩 움직입니다. 
# 루돌프가 한 번 움직인 뒤, 1번 산타부터 P번 산타까지 순서대로 움직이게 됩니다. 
# 이때 기절해있거나 격자 밖으로 빠져나가 게임에서 탈락한 산타들은 움직일 수 없습니다.



# < 상호작용 >
# 루돌프와의 충돌 후 산타는 포물선의 궤적으로 이동하여 착지하게 되는 칸에서만 상호작용이 발생할 수 있습니다.
# 산타는 충돌 후 착지하게 되는 칸에 다른 산타가 있다면 그 산타는 1칸 해당 방향으로 밀려나게 됩니다.
# 그 옆에 산타가 있다면 연쇄적으로 1칸씩 밀려나는 것을 반복하게 됩니다. 게임판 밖으로 밀려나오게 된 산타의 경우 게임에서 탈락됩니다.

# < 기절 >
# 산타는 루돌프와의 충돌 후 기절을 하게 됩니다. 
# 현재가 k번째 턴이었다면, (k+1)번째 턴까지 기절하게 되어 (k+2)번째 턴부터 다시 정상상태가 됩니다.
# 기절한 산타는 움직일 수 없게 됩니다. 단, 기절한 도중 충돌이나 상호작용으로 인해 밀려날 수는 있습니다.
# 루돌프는 기절한 산타를 돌진 대상으로 선택할 수 있습니다.

# < 게임종료 >
# M 번의 턴에 걸쳐 루돌프, 산타가 순서대로 움직인 이후 게임이 종료됩니다.
# 만약 P 명의 산타가 모두 게임에서 탈락하게 된다면 그 즉시 게임이 종료됩니다.
# 매 턴 이후 아직 탈락하지 않은 산타들에게는 1점씩을 추가로 부여합니다.

# 출력 : 게임이 끝났을 때 각 산타가 얻은 최종 점수



import sys

input = sys.stdin.readline

N, M, P, C, D = map(int,input().split())

rx, ry = map(int,input().split())

area = [[0]*N for _ in range(N)]

dx, dy = [-1,0,1,0], [0,1,0,-1]

santa_list = []

score = [0]*(P+1)

# (처음 산타와 루돌프의 위치는 겹쳐져 주어지지 않음)

def debug():
    for a in area:
        print(a)
    print()

def cal(x1,y1,x2,y2): # 거리 계산 함수
    return (x1-x2)**2 + (y1-y2)**2


def get_santa(): # 가장 가까운 산타를 구하는 함수
    
    info = [] # (거리, 행 r, 열 c)
    
    for santa_index, sx, sy in santa_list:
        if santa_index == -1 and sx == -1 and sy == -1:
            continue
        info.append((cal(rx,ry,sx,sy), sx, sy,santa_index))
    info.sort(key = lambda x:(x[0],-x[1],-x[2]))
    
    if info:
        return info[0]
    else:
        return []

# < 루돌프의 움직임 >
# 1. 게임에서 탈락하지 않은 산타 중 가장 가까운 산타를 향해 1칸 돌진
# 2. 만약 가장 가까운 산타가 2명 이상이라면, r 좌표가 큰 산타를 향해 돌진, r이 동일한 경우 c 좌표가 큰 산타를 향해 돌진
# (거리, 행 r, 열 c)
# 3. 루돌프는 상하좌우, 대각선을 포함한 인접한 8방향 중 하나로 돌진
# (편의상 인접한 대각선 방향으로 전진하는 것도 1칸 전진하는 것이라 생각)
# 가장 우선순위가 높은 산타를 향해 8방향 중 가장 가까워지는 방향으로 한 칸 돌진합니다.
def move_to_santa(x,y,sx,sy):
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
# 산타는 1번부터 P번까지 순서대로 움직입니다.
# 기절했거나 이미 게임에서 탈락한 산타는 움직일 수 없습니다.
# 산타는 루돌프에게 거리가 가장 가까워지는 방향으로 1칸 이동합니다.
# 산타는 다른 산타가 있는 칸이나 게임판 밖으로는 움직일 수 없습니다.
# 움직일 수 있는 칸이 없다면 산타는 움직이지 않습니다.
# 움직일 수 있는 칸이 있더라도 만약 루돌프로부터 가까워질 수 있는 방법이 없다면 산타는 움직이지 않습니다.
# 산타는 상하좌우로 인접한 4방향 중 한 곳으로 움직일 수 있습니다. 
# 이때 가장 가까워질 수 있는 방향이 여러 개라면, 상우하좌 우선순위에 맞춰 움직입니다.
def move_to_rudol(x,y,rx,ry,santa_index):

    current_dis = cal(x,y,rx,ry)

    info = [] # (거리, 방향 인덱스) # 이때 가장 가까워질 수 있는 방향이 여러 개라면, 상우하좌 우선순위에 맞춰 움직입니다.

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < N and 0 <= ny < N and (area[nx][ny] == 0 or area[nx][ny] == -1) : # 산타는 다른 산타가 있는 칸이나 게임판 밖으로는 움직일 수 없습니다.
            dis = cal(nx,ny,rx,ry)
            # print("nx,ny,dis,rx,ry : ",nx,ny,dis,rx,ry)
            if dis < current_dis:
                info.append((dis,i,nx,ny,santa_index))
    #print(current_dis)
    info.sort(key = lambda x:(x[0],x[1]))
    # print(info) # [(0, 0, 3, 0)]
    if info:
        return info[0]
    else:
        return []


def interact(x,y,dx,dy,si):

    # print("inter:",x,y,dx,dy,si)

    temp = area[x][y]
    next_x, next_y = x + dx, y + dy
    area[x][y] = si
    santa_list[si-1] = (si,x,y)

    if 0 <= next_x < N and 0 <= next_y < N: # 범위 밖으로 안 나가는 경우
        if area[next_x][next_y] != 0 and area[next_x][next_y] != -1: # 또 다른 산타가 있다면
            interact(next_x,next_y,dx,dy,temp)
        else: # 산타가 없으면
            area[next_x][next_y] = temp
            santa_list[temp-1] = (temp,next_x,next_y)
    else: # 범위 밖으로 나가는 경우
        santa_list[temp-1] = (-1,-1,-1)


# < 충돌 >
# 산타와 루돌프가 같은 칸에 있게 되면 충돌이 발생합니다.
# 1. 루돌프가 움직여서 충돌이 일어난 경우, 해당 산타는 C만큼의 점수를 얻게 됩니다.
# 이와 동시에 산타는 루돌프가 이동해온 방향으로 C 칸 만큼 밀려나게 됩니다.
# 2. 산타가 움직여서 충돌이 일어난 경우, 해당 산타는 D만큼의 점수를 얻게 됩니다. 
# 이와 동시에 산타는 자신이 이동해온 반대 방향으로 D 칸 만큼 밀려나게 됩니다.
# [[ 밀려나는 것은 포물선 모양을 그리며 밀려나는 것이기 때문에 이동하는 도중에 충돌이 일어나지는 않고 정확히 원하는 위치에 도달하게 됩니다. ]]
# 만약 밀려난 위치가 게임판 밖이라면 산타는 게임에서 탈락됩니다.
# 만약 밀려난 칸에 다른 산타가 있는 경우 '상호작용'이 발생합니다.

def crash_r_to_s(rx,ry,sx,sy,santa_index,dx,dy): # 1. 루돌프가 움직여서 충돌이 일어난 경우, 해당 산타는 C만큼의 점수를 얻게 됩니다.
    
    score[santa_index] += C

    next_x, next_y = sx + (dx*C), sy + (dy*C)

    area[rx][ry] = -1

    # print(next_x,next_y)

    # debug()

    if 0 <= next_x < N and 0 <= next_y < N:
        if area[next_x][next_y] != 0 and area[next_x][next_y] != -1:
            interact(next_x,next_y,dx,dy,santa_index)
        else:
            area[next_x][next_y] = santa_index
    else:
        santa_list[santa_index-1] = (-1,-1,-1)

def crash_s_to_r(rx,ry,sx,sy,santa_index,dx,dy): # 2. 산타가 움직여서 충돌이 일어난 경우, 해당 산타는 D만큼의 점수를 얻게 됩니다. 
    score[santa_index] += D
    next_x, next_y = sx + (-dx*C), sy + (-dy*C)
    # print("sibal",next_x,next_y)

    # area[rx][ry] = santa_index

    if 0 <= next_x < N and 0 <= next_y < N:
        if area[next_x][next_y] != 0 and area[next_x][next_y] != -1:
            interact(next_x,next_y,-dx,-dy,santa_index)
        else:
            area[next_x][next_y] = santa_index

    else:
        santa_list[santa_index-1] = (-1,-1,-1)  

rx -= 1
ry -= 1

for _ in range(P):
    santa_i, sx, sy = map(int,input().split())
    sx -= 1
    sy -= 1
    area[sx][sy] = santa_i # 산타(인덱스)
    santa_list.append((santa_i,sx,sy))

area[rx][ry] = -1 # 루돌프(-1)

for _ in range(M):

    debug()

    santa_info = get_santa() # (5, 4, 0, 3)

    # print(santa_info)
    if not santa_info:
        continue


    result_1 = move_to_santa(rx,ry,santa_info[1],santa_info[2]) # (3, 0, 1, -1)
    # print(result_1)
    if result_1:
        next_rx, next_ry, d1, d2 = result_1

    area[rx][ry] = 0

    if area[next_rx][next_ry] != 0 and area[next_rx][next_ry] != -1: # 충돌한 경우
        crash_r_to_s(next_rx,next_ry,next_rx,next_ry,area[next_rx][next_ry],d1,d2)
    else: # 충돌하지 않은 경우
        area[next_rx][next_ry] = -1
        rx = next_rx
        ry = next_ry

    
    # 충돌

    for si, sx, sy in santa_list:
        # debug()
        # temp_area = [x[:] for x in area]
        if si == -1 and sx == -1 and sy == -1:
            continue
        # print("hi",si,sx,sy)
        result_2 = move_to_rudol(sx,sy,rx,ry,si) # # [(0, 0, 3, 0,n)] (거리,방향인덱스,도착x,도착y,산타인덱스)
        # print("help",si,result_2)
        if not result_2:
            continue
        d, di, nx, ny, si = result_2

        area[sx][sy] = 0

        if area[nx][ny] == -1: # 충돌한 경우
            # print("hello")
            crash_s_to_r(nx,ny,nx,ny,si,dx[di],dy[di])
        else:
            area[nx][ny] = si
            santa_list[si-1] = (si,nx,ny)
        # temp_area[sx][sy] =
    # debug()
    # print(rx,ry)
    # print(santa_list)




# print(santa_list) # [(1, 0, 2), (2, 2, 4), (3, 3, 0), (4, 3, 3)]



# debug()

# santa_info = get_santa() # (5, 4, 0, 3)
# # print(santa_info)

# # print(move_to_santa(rx,ry,santa_info[1],santa_info[2]))
# result_1 = move_to_santa(rx,ry,santa_info[1],santa_info[2]) # (3, 0, 1, -1)
# if result_1:
#     next_rx, next_ry, d1, d2 = result_1

# area[rx][ry] = 0

# if area[next_rx][next_ry] != 0 and area[next_rx][next_ry] != -1: # 충돌한 경우
#     crash_r_to_s(next_rx,next_ry,next_rx,next_ry,area[next_rx][next_ry],d1,d2)

# else: # 충돌하지 않은 경우
#     area[next_rx][next_ry] = -1
#     rx = next_rx
#     ry = next_ry

# debug()
# # 충돌

# for si, sx, sy in santa_list:
#     # temp_area = [x[:] for x in area]
#     result_2 = move_to_rudol(sx,sy,rx,ry,si) # # [(0, 0, 3, 0,n)] (거리,방향인덱스,도착x,도착y,산타인덱스)
#     if not result_2:
#         continue
#     d, di, nx, ny, si = result_2

#     area[sx][sy] = 0

#     if area[nx][ny] == -1: # 충돌한 경우
#         crash_s_to_r(nx,ny,nx,ny,si,dx[di],dy[di])
#     else:
#         area[nx][ny] = si
#     # temp_area[sx][sy] =
# debug()


# print(santa_list)