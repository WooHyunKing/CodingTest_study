import sys

input = sys.stdin.readline

# M명의 참가자가 미로 탈출하기 게임에 참가

# < 미로의 구성 >
# N x N 크기의 격자, 각 칵은 [빈칸 / 벽 / 출구] 로 구성

# 빈칸 : 참가자가 이동 가능한 칸
# 벽 : 참가자가 이동할 수 없는 칸, 1~9 이하의 내구도를 가지고 있음
# 회전할 때 내구도가 1 씩 깎임, 내구도가 0이 되면 빈칸으로 변경
# 출구 : 참가자가 해당 칸에 도착하면 즉시 탈출

# 위 과정을 K초 동안 반복
# 단, K초 전에 모든 참가자가 탈출에 성공한다면 게임이 끝난다.
# 게임이 끝났을 때, [모든 참가자들의 이동 거리의 합]과 [출구 좌표]를 출력

# 두 위치간의 최단거리는 abs(x1-x2) + abs(y1-y2)로 정의
def calculate_dis(x1,y1,x2,y2):
    return abs(x1-x2) + abs(y1-y2)

N, M, K = map(int,input().split())

# 빈칸 : 0, 1~9 : 벽 내구도
area = [list(map(int,input().split())) for _ in range(N)]

dx, dy = [-1,1,0,0], [0,0,-1,1]

answer = 0

INF = float("inf")

# 참가자들의 좌표(모든 참가자는 빈칸에서 시작)
players = []

players_status = [False]*M

for _ in range(M):
    px, py = map(int,input().split())
    players.append([px-1,py-1])

# 출구 좌표(빈칸에만 존재, 참가자와 겹치지 않음)
end_x, end_y = map(int,input().split())
end_x, end_y = end_x - 1, end_y - 1

area[end_x][end_y] = INF

# 종료 조건 : 게임 시작 후 K초가 지났거나, 모든 참가자가 미로를 탈출했을 때
# 출력 : 모든 참가자들의 이동거리의 합 + 출구 좌표

def partial_rotate90(area,x,y,d):

    global end_x, end_y

    temp_area = [x[:] for x in area]

    moved_end = False
    moved_players = [False]*M

    for i in range(d):
        for j in range(d):
            if 1 <= area[x+i][y+j] <= 9:
                temp_area[x+j][y+d-1-i] = area[x+i][y+j]-1
            else:
                temp_area[x+j][y+d-1-i] = area[x+i][y+j]

            if not moved_end and x+i == end_x and y+j == end_y:
                end_x = x+j
                end_y = y+d-1-i
                moved_end = True

            for pi in range(M):
                if not moved_players[pi] and not players_status[pi] and players[pi][0] == x+i and players[pi][1] == y+j:
                    players[pi] = [x+j,y+d-1-i]
                    moved_players[pi] = True

    return temp_area

for main_index in range(K):

    # 1) 참가자의 이동

    # 1초마다 모든 참가자는 한 칸씩 움직인다.
    # 모든 참가자는 동시에 움직인다.
    # 상하좌우로 움직일 수 있으며, [벽이 없는 곳]으로 이동할 수 있다.
    # 움직인 칸은 현재 머물러 있던 칸보다 출구까지의 최단 거리가 가까워야 한다.
    # 움직일 수 있는 칸이 2개 이상이라면, [상하로 움직이는 것]을 우선시 한다 !!
    # 참가자가 움직일 수 없는 상황이라면, 움직이지 않는다.
    # 한 칸에 2명 이상의 참가자가 있을 수 있다.

    # 우선순위 : 거리(-) > 상하 이동

    for i, value in enumerate(players):

        if players_status[i]:
            continue

        cx, cy = value[0], value[1]

        current_dis = calculate_dis(cx,cy,end_x,end_y)

        cases = []
        
        for di in range(4):
            nx, ny = cx + dx[di], cy + dy[di]

            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            
            # 벽으로 이동할 수 없다.
            if 1 <= area[nx][ny] <= 9:
                continue

            next_dis = calculate_dis(nx,ny,end_x,end_y)
            
            # 움직인 칸은 현재 머물러 있던 칸보다 출구까지의 최단 거리가 가까워야 한다.
            if next_dis >= current_dis:
                continue

            cases.append((next_dis,nx,ny,di))
        
        # 참가자가 움직일 수 없는 상황이라면, 움직이지 않는다.
        if len(cases) == 0:
            continue
        
        cases.sort(key = lambda x:(-x[0], -x[3]))

        next_x, next_y = cases[-1][1], cases[-1][2]

        players[i] = [next_x, next_y]
        answer += 1

        # 출구에 도착했을 경우
        if next_x == end_x and next_y == end_y:
            players_status[i] = True
    
    # 2) 미로의 회전

    # 모든 참가자가 이동을 끝냈으면, 다음 조건에 의해 미로가 회전한다.

    # 1명 이상의 참가자와 출구를 포함한 가장 작은 정사각형을 잡는다.
    # 가장 작은 크기를 갖는 정사각형이 2개 이상이라면 [좌상단 r 좌표가 가장 작은 것]이 우선되고,
    # 그래도 같으면 [좌상단 c 좌표가 작은 것]이 우선된다.
    # 선택된 정사각형은 시계방향으로 90도 회전하며, 회전된 벽은 내구도가 1씩 깎인다.

    # 우선순위 : 정사각형 크기(-) > r좌표(-) > c좌표(-)

    miro_cases = []

    for i in range(N):
        for j in range(N):
            for length in range(1,N+1):
                ni, nj = i+length, j+length

                coors = set()

                if ni < 0 or nj < 0 or ni >= N or nj >= N:
                    break

                for x in range(i,ni+1):
                    for y in range(j,nj+1):
                        coors.add((x,y))
                
                # 출구가 없으면 제외
                if (end_x, end_y) not in coors:
                    continue

                have_player = False

                for pi, value in enumerate(players):
                    # 이미 탈출한 참가자는 제외
                    if players_status[pi]:
                        continue
                    
                    if (value[0],value[1]) in coors:
                        have_player = True
                        break
                
                # 참가자가 없으면 제외
                if not have_player:
                    continue

                miro_cases.append((length+1, i,j))
    
    if len(miro_cases) == 0:
        break

    miro_cases.sort(key = lambda x:(-x[0], -x[1], -x[2]))

    rect_length, rect_x, rect_y = miro_cases[-1][0], miro_cases[-1][1], miro_cases[-1][2]

    area = partial_rotate90(area,rect_x, rect_y,rect_length)
                
print(answer)
print(end_x+1, end_y+1)