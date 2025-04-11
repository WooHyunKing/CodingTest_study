import sys

from collections import deque

input = sys.stdin.readline

# 1. 게임판의 구성
# N x N 크기의 격자로 이루어져 있음
# 게임은 총 M개의 턴에 걸쳐서 진행되며, 매 턴마다 루돌프와 산타들이 1번씩 움직인다.
# 루돌프가 1번 움직인 뒤, 1번부터 P번 산타들이 '순서대로' 움직인다.
# 이때 기절해있거나 격자 밖으로 빠져나가 게임에서 탈락한 산타는 움직일 수 X !!

# 4. 충돌
# 산타와 루돌프가 같은 칸에 있게 되면 충돌이 발생한다.
    # 4-1. 루돌프가 움직여서 충돌이 일어난 경우
    # 해당 산타는 C만큼의 점수를 얻게 된다.
    # 이와 동시에, 산타는 루돌프가 이동해온 방향으로 C칸 만큼 밀려난다.

    # 4-2. 산타가 움직여서 충돌이 일어난 경우
    # 해당 산타는 D만큼의 점수를 얻게 된다.
    # 이와 동시에, 산타는 자신이 이동해온 반대 방향으로 D칸 만큼 밀려난다.

    # (밀려나는 것은 포물선을 그리며 밀려나는 것이기 때문에 이동 중에 충돌이 일어나지 않고 정확히 원하는 위치에 도달)
    # 만약에 밀려난 위치가 게임판 밖이라면 산타는 게임에서 탈락한다.
    # 만약 밀려난 칸에 다른 산타가 있는 경우,[상호작용]이 발생한다.

# 5. 상호작용
# 루돌프와의 충돌 후 밀려난 칸에서만 상호작용이 발생
# 산타는 충돌 후 착지하는 칸에 다른 산타가 있다면, 그 산타는 해당 방향으로 1칸 밀려난다.
# 그 옆에 산타가 있다면 [연쇄적]으로 1칸씩 밀려난다.

# 게임판 밖으로 밀려나오게 된 산타는 게임에서 탈락한다.

# 6. 기절
# 산타는 루돌프와의 충돌 후 기절을 하게 된다.
# 현재가 k번째 턴이라면 다음 턴(k+1번째 턴)까지 기절하게 된다.
# 즉, 다다음 턴인 k+2번째 턴부터 다시 정상 상태가 된다.

# 기절한 산타는 움직일 수 없다.
# (단, 기절한 도중에 충돌이나 상호작용으로 인해 밀려날 수는 있다.)
# 루돌프는 기절한 산타를 돌진 대상으로 선택할 수 있다.

# 출력 : 각 산타가 얻은 최종 점수

# 게임판에서 두 칸 사이의 거리는 (r1-r2)^2 + (c1-c2)^2 로 계산
def calculate_distance(x1,y1,x2,y2):
    return (x1-x2)**2 + (y1-y2)**2

# 게임 판 크기 / 게임 턴 수 / 산타 수 / 루돌프 힘 / 산타 힘
N, M, P, C, D = map(int,input().split())

INF = float("inf")

area = [[0]*N for _ in range(N)]

dx, dy = [-1,0,1,0],[0,1,0,-1] # 상 우 하 좌
dx2, dy2 = [-1,-1,0,1,1,1,0,-1], [0,1,1,1,0,-1,-1,-1] # 대각선 포함

# 루돌프의 초기 위치
rr, rc = map(int,input().split())
rx, ry = rr-1, rc-1

area[rx][ry] = INF

santa_coor = [[] for _ in range(P+1)]

santa_score = [0]*(P+1)

# -1 이면 사망, 0이면 정상, 1이상 이면 기절
santa_status = [0]*(P+1)

def get_shortest_coor_for_rodul(sx,sy,dx,dy):

    cases = []

    for i in range(8):
        nx, ny = sx + dx2[i], sy + dy2[i]

        if nx < 0 or ny < 0 or nx >= N or ny >= N:
            continue

        distance = calculate_distance(dx,dy,nx,ny)
        
        cases.append((distance,nx,ny,i))
    
    cases.sort(key = lambda x : -x[0])

    return cases[-1][1], cases[-1][2], cases[-1][3]

for _ in range(P):
    santa_index, sr, sc = map(int,input().split())
    sr, sc = sr-1, sc-1
    santa_coor[santa_index] = [sr,sc]
    area[sr][sc] = santa_index

for _ in range(M):

    # 2. 루돌프의 움직임
    # 루돌프는 상하좌우, 대각선을 포함한 인접한 8방향 중 하나로 돌진할 수 있다.
    # 루돌프는 가장 가까운 산타를 향해 1칸 돌진한다.
    # (단, 게임에서 탈락하지 않은 산타 중 가장 가까운 산타를 선택해야 한다.)
    # 만약 가장 가까운 산타가 2명 이상이라면 [거리->r->c] 순으로 우선순위를 가진다.

    next_santa_list = []

    for i in range(1,P+1):
        
        sx, sy = santa_coor[i]
        s_status = santa_status[i]
        
        # 탈락한 산타는 제외
        if s_status == -1:
            continue
        
        distance = calculate_distance(rx,ry,sx,sy)

        next_santa_list.append((distance,sx,sy))
    
    # 만약 P명의 산타가 모두 게임에서 탈락하게 된다면 그 즉시 게임이 종료된다.
    if len(next_santa_list) == 0:
        break
    
    next_santa_list.sort(key = lambda x : [-x[0],x[1],x[2]])

    next_santa = next_santa_list[-1]

    next_sx, next_sy = next_santa[1], next_santa[2]

    temp_rx, temp_ry = rx, ry

    next_rx, next_ry, direction = get_shortest_coor_for_rodul(rx,ry,next_sx,next_sy)

    # 4-1. 루돌프가 움직여서 충돌이 일어난 경우
    # 해당 산타는 C만큼의 점수를 얻게 된다.
    # 이와 동시에, 산타는 루돌프가 이동해온 방향으로 C칸 만큼 밀려난다.
    if area[next_rx][next_ry] != 0:
        crash_santa_index = area[next_rx][next_ry]
        
        santa_score[crash_santa_index] += C

        # 튕겨지는 x좌표, y좌표, 튕겨나가는 거리
        santa_q = deque([(next_rx, next_ry, C, crash_santa_index)])

        while santa_q:
            current_x, current_y, dis, index = santa_q.popleft()

            next_x, next_y = current_x + (dis*dx2[direction]), current_y + (dis*dy2[direction])

            # 만약에 밀려난 위치가 게임판 밖이라면 산타는 게임에서 탈락한다.
            if next_x < 0 or next_y < 0 or next_x >= N or next_y >= N:
                santa_status[index] = -1
                continue

            # 만약 밀려난 칸에 다른 산타가 있는 경우,[상호작용]이 발생한다.
            if 1 <= area[next_x][next_y] <= 31:
                santa_q.append((next_x, next_y, 1, area[next_x][next_y]))
            
            area[next_x][next_y] = index
            santa_coor[index] = [next_x,next_y]
        
        # 밀려난 산타가 탈락하지 않았다면 기절
        if santa_status[crash_santa_index] != -1:
            santa_status[crash_santa_index] = 2
    
    area[temp_rx][temp_ry] = 0
    area[next_rx][next_ry] = INF
    rx, ry = next_rx, next_ry

    # ------------ 루돌프 이동 완료 --------------

    # 3. 산타의 움직임

    # 산타는 상하좌우로 움직일 수 있다.
    # 산타는 1번부터 P번까지 순서대로 움직인다.
    # (단, 기절해있거나 이미 게임에서 탈락한 산타는 움직일 수 없다.)
    # 산타는 루돌프에게 거리가 가장 가까워지는 방향으로 1칸 이동한다.
    # 가장 가까워질 수 있는 방향이 여러 개라면, [상->우->하->좌] 의 우선순위를 가진다.

    # 움직일 수 있는 칸이 없다면 산타는 움직이지 않는다.
    # 움직일 수 있는 칸이 있더라도 루돌프로부터 가까워질 수 있는 방법이 없다면 산타는 움직이지 않는다.

    for i in range(1,P+1):
        sx, sy = santa_coor[i]
        s_status = santa_status[i]
        
        # 탈락하거나 기절한 산타는 제외
        if s_status == -1 or s_status >= 1:
            continue
        
        current_dis = calculate_distance(sx,sy,rx,ry)

        cases = []
    
        for di in range(4):
            nx, ny = sx + dx[di], sy + dy[di]

            # 산타는 다른 산타가 있는 칸이나 게임판 밖으로는 움직일 수 없다.
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if 1 <= area[nx][ny] <= 31:
                continue
            
            next_dis = calculate_distance(nx,ny,rx,ry)

            if next_dis < current_dis:
                cases.append((next_dis,nx,ny,di))
        
        # 움직일 수 있는 칸이 없다면 산타는 움직이지 않는다.
        if len(cases) == 0:
            continue
        
        cases.sort(key = lambda x : [-x[0],-x[3]])

        next_santa_info = cases[-1]

        next_santa_x, next_santa_y, direction_s = next_santa_info[1], next_santa_info[2], next_santa_info[3]

        # 4-2. 산타가 움직여서 충돌이 일어난 경우
        # 해당 산타는 D만큼의 점수를 얻게 된다.
        # 이와 동시에, 산타는 자신이 이동해온 반대 방향으로 D칸 만큼 밀려난다.

        # (밀려나는 것은 포물선을 그리며 밀려나는 것이기 때문에 이동 중에 충돌이 일어나지 않고 정확히 원하는 위치에 도달)
        # 만약에 밀려난 위치가 게임판 밖이라면 산타는 게임에서 탈락한다.
        # 만약 밀려난 칸에 다른 산타가 있는 경우,[상호작용]이 발생한다.

        if area[next_santa_x][next_santa_y] == INF:

            santa_score[i] += D

            area[sx][sy] = 0

            # 상 -> 하
            if direction_s == 0:
                direction_s = 2
            # 우 -> 좌
            elif direction_s == 1:
                direction_s = 3
            # 하 -> 상
            elif direction_s == 2:
                direction_s = 0
            # 좌 -> 우
            elif direction_s == 3:
                direction_s = 1
            
            santa_q2 = deque([(next_santa_x, next_santa_y,D,i)])

            while santa_q2:
                current_sx, current_sy, d_dis, current_index = santa_q2.popleft()

                next_sx_2, next_sy_2 = current_sx + (d_dis*dx[direction_s]), current_sy + (d_dis*dy[direction_s])

                if next_sx_2 < 0 or next_sy_2 < 0 or next_sx_2 >= N or next_sy_2 >= N:
                    santa_status[current_index] = -1
                    continue
                
                # 만약 밀려난 칸에 다른 산타가 있는 경우,[상호작용]이 발생한다.
                if 1 <= area[next_sx_2][next_sy_2] <= 31:
                    santa_q2.append((next_sx_2, next_sy_2, 1, area[next_sx_2][next_sy_2]))

                area[next_sx_2][next_sy_2] = current_index
                santa_coor[current_index] = [next_sx_2, next_sy_2]
            
            # 밀려난 산타가 탈락하지 않았다면 기절
            if santa_status[i] != -1:
                santa_status[i] = 2
        
        else:
            area[next_santa_x][next_santa_y] = i
            santa_coor[i] = [next_santa_x,next_santa_y]
            area[sx][sy] = 0

    for i in range(1,P+1):
        # 매 턴 이후 아직 탈락하지 않은 산타들에게는 1점씩 점수를 부여한다.
        if santa_status[i] != -1:
            santa_score[i] += 1

        # 기절 카운팅 -1
        if santa_status[i] >= 1:
            santa_status[i] -= 1

# 7. 게임 종료
# M번의 턴에 걸쳐 루돌프와 산타가 순서대로 움직인 후 게임이 종료된다.

for i in range(1,P+1):
    print(santa_score[i], end=" ")