# N x N 크기의 마을에 도로가 깔려있다. (도로는 0, 비도로는 1)
# 집에서 공원까지 산책
# 메두사는 오직 도로만을 따라 최단 경로로 공원까지 이동
# 메두사의 집과 공원은 항상 도로 위에 있으며(좌표는 서로 다르다고 가정해도 ok)

# M명의 전사들이 메두사를 잡기 위해 최단 경로로 이동
# 전사들은 도로와 비도로를 구분하지 않고 어느 칸이든 이동 가능
# (메두사의 집에 전사들이 초기에 위치하는 경우는 없다고 가정해도 ok)

# 메두사는 전사들이 움직이기 전에 그들을 바라봄으로써 돌로 만들어 움직임을 멈출 수 있다.

# # # 모든 최단경로 계산은 '맨해튼 거리'를 기준으로 한다 ! ! ! ! !

# 1. 메두사의 이동

# 메두사는 도로를 따라 1칸 이동하며 공원까지 최단 경로를 따른다. 
# (만약 집에서 공원까지 최단경로가 여러개라면 상->하->좌->우의 우선 순위를 따른다.)
# (메두사의 집으로부터 공원까지 도달하는 경로가 없을 수도 있음.)
# 메두사가 이동한 칸에 전사가 있을 경우 전사는 사라진다.

# 2. 메두사의 시선
# 상/하/좌/우 하나의 방향을 선택해서 바라본다.

# 메두사는 바라보는 방향으로 90도의 시야각을 가지며, 시야각 범위 안에 있는 전사들을 볼 수 있다.
# 메두사의 시야각 안에 있지만, 다른 전사에게 가려진 경우 피할 수 있다.
# (메두사로부터 8방향 중 한 방향에 전사가 있다면, 그 전사가 동일한 방향으로 바라보는 범위의 칸은 안전하다.)

# 메두사가 본 전사들은 모두 돌로 변해서 현재 턴에는 움직일 수 없으며, 해당 턴이 종료되면 돌에서 풀려난다.
# (만약 2명 이상의 전사들이 같은 칸에 위치해있다면 해당 칸의 전사들은 모두 돌로 변한다.)

# 이때, 메두사는 상/하/좌/우 중 전사를 가장 많이 볼 수 있는 방향을 바라본다.
# (전사의 수가 같다면, 상->하->좌->우의 우선순위로 방향을 결정한다.)


# 3. 전사들의 이동
# 돌로 변하지 않은 병사들은 메두사를 향해 최대 2칸 이동한다.
# 전사들은 이동 중 같은 칸을 공유할 수 있다.

    # 3-1. 메두사와의 거리를 줄일 수 있는 방향으로 1칸 이동한다. 
    # (이런 방향이 2개 이상이면 상->하->좌->우의 우선순위로 방향을 선택한다.)
    # 격자 바깥으로 나갈 수 없고, 메두사의 시야에 들어오는 곳으로는 이동할 수 없다.

    # 3-2. 메두사와의 거리를 줄일 수 있는 방향으로 1칸 이동한다. 
    # (이런 방향이 2개 이상이면 좌->우->상->하의 우선순위로 방향을 선택한다.)

# 4. 전사의 공격
# 메두사와 같은 칸에 도달한 전사는 사라진다.

# 위 네 단계가 반복되어 메두사가 공원에 도달할 때까지 매 턴마다 
# [모든 전사가 이동한 거리의 합], [메두사로 인해 돌이 된 전사의 수], [메두사를 공격한 전사의 수]
# 를 공백을 사이에 두고 차례대로 출력

# 단, 메두사가 공원에 도착하는 턴에는 0을 출력하고 프로그램을 종료
# 만약에 메두사의 집으로부터 공원까지 이어지는 도로가 존재하지 않으면 -1 출력

from collections import deque
import sys

N, M = map(int,input().split())

INF = float("inf")

input = sys.stdin.readline

mx, my, px, py = map(int,input().split())

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
dx2, dy2 = [0,0,-1,1], [-1,1,0,0]

warrior_coors = list(map(int,input().split()))
warriors = []
warriors_status = dict() # 0 이면 생존, -1 이면 사망, 1 이면 석화

current_sight_grid = [[0 for _ in range(N)] for _ in range(N)] # 2이면 안전지대, 0 이면 보류, 1이면 위험지대

for i in range(0,M*2,2):
    warriors.append([warrior_coors[i],warrior_coors[i+1]])

for i in range(M):
    warriors_status[i] = 0

area = [list(map(int,input().split())) for _ in range(N)]

def compute_distance(sx, sy, area): # BFS를 이용하여 종료 지점에서부터 모든 셀 까지의 최단 거리를 계산하여 반환하는 함수
    distance = [[INF if area[i][j] else -1 for j in range(N)] for i in range(N)]

    queue = deque()
    queue.append((sx,sy))
    
    distance[sx][sy] = 0

    while queue:
        cx, cy = queue.popleft()

        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            if distance[nx][ny] != -1:
                continue

            distance[nx][ny] = distance[cx][cy] + 1
            
            queue.append((nx,ny))
    
    return distance

def compute_distance_w(sx, sy): # BFS를 이용하여 종료 지점에서부터 모든 셀 까지의 최단 거리를 계산하여 반환하는 함수
    distance = [[INF for _ in range(N)] for _ in range(N)]

    queue = deque()
    queue.append((sx,sy))
    
    distance[sx][sy] = 0

    while queue:
        cx, cy = queue.popleft()

        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            if distance[nx][ny] != INF:
                continue

            distance[nx][ny] = distance[cx][cy] + 1
            
            queue.append((nx,ny))
    
    return distance

def sight_down(x,y,isTest):

    global current_sight_grid

    sight_grid = [[0 for _ in range(N)] for _ in range(N)] # 2이면 안전지대, 0 이면 보류, 1이면 위험지대

    count = 0

    for i in range(x+1,N):
        left = max(y-(i-x), 0)
        right = min(y+(i-x), N-1)

        for j in range(left, right+1):

            if sight_grid[i][j] == 2:
                continue

            sight_grid[i][j] = 1

            for w in range(M):

                if warriors_status[w] != -1 and warriors[w][0] == i and warriors[w][1] == j: # 시야에 전사가 있는 경우
                    if not isTest:
                        warriors_status[w] = 1 # 석화시키기
                    count += 1
                    
                    if j < y: # 왼쪽 대각선
                        for k in range(i+1,N):
                            temp_left = max(j - (k-i), 0)
                            temp_right = j

                            for d in range(temp_left, temp_right+1):
                                sight_grid[k][d] = 2
                    
                    elif j == y: # 아래
                        for k in range(i+1,N):
                            sight_grid[k][j] = 2

                    elif j > y: # 오른쪽 대각선
                        for k in range(i+1,N):
                            temp_left = j
                            temp_right = min(j+(k-i),N-1)

                            for d in range(temp_left, temp_right+1):
                                sight_grid[k][d] = 2

    if not isTest:
        current_sight_grid = sight_grid

    return count

def sight_up(x,y,isTest):

    global current_sight_grid

    sight_grid = [[0 for _ in range(N)] for _ in range(N)] # 2이면 안전지대, 0 이면 보류, 1이면 위험지대

    count = 0

    for i in range(x-1,-1,-1):

        left = max(y+(i-x), 0)
        right = min(y-(i-x), N-1)

        for j in range(left, right+1):

            if sight_grid[i][j] == 2:
                continue

            sight_grid[i][j] = 1

            for w in range(M):

                if warriors_status[w] != -1 and warriors[w][0] == i and warriors[w][1] == j: # 시야에 전사가 있는 경우
                    if not isTest:
                        warriors_status[w] = 1 # 석화시키기
                    count += 1

                    if j < y: # 왼쪽 대각선
                        for k in range(i-1,-1,-1):
                            temp_left = max(j+(k-i), 0)
                            temp_right = j

                            for d in range(temp_left, temp_right+1):
                                sight_grid[k][d] = 2
                    
                    elif j == y: # 위
                        for k in range(i-1,-1,-1):
                            sight_grid[k][j] = 2

                    elif j > y: # 오른쪽 대각선
                        for k in range(i-1,-1,-1):
                            temp_left = j
                            temp_right = min(j-(k-i),N-1)

                            for d in range(temp_left, temp_right+1):
                                sight_grid[k][d] = 2

    if not isTest:
        current_sight_grid = sight_grid
    return count

def sight_left(x,y,isTest):

    global current_sight_grid

    sight_grid = [[0 for _ in range(N)] for _ in range(N)] # 2이면 안전지대, 0 이면 보류, 1이면 위험지대

    count = 0

    for j in range(y-1,-1,-1):
        top = max(x+(j-y),0)
        bottom = min(x-(j-y),N-1)

        for i in range(top,bottom+1):
            
            if sight_grid[i][j] == 2:
                continue

            sight_grid[i][j] = 1

            for w in range(M):

                if warriors_status[w] != -1 and warriors[w][0] == i and warriors[w][1] == j: # 시야에 전사가 있는 경우
                    if not isTest:
                        warriors_status[w] = 1 # 석화시키기
                    count += 1

                    if i < x: # 위 대각선
                        for k in range(j-1,-1,-1):
                            top = max(i+(k-j),0)
                            bottom = i

                            for d in range(top, bottom+1):
                                sight_grid[d][k] = 2

                    elif i == x: # 왼쪽
                        for k in range(j-1,-1,-1):
                            sight_grid[i][k] = 2
                    
                    elif i > x : # 아래 대각선
                        for k in range(j-1,-1,-1):
                            top = i
                            bottom = min(i-(k-j),N-1)

                            for d in range(top, bottom+1):
                                sight_grid[d][k] = 2

    if not isTest:
        current_sight_grid = sight_grid
    return count

def sight_right(x,y,isTest):

    global current_sight_grid

    sight_grid = [[0 for _ in range(N)] for _ in range(N)] # 2이면 안전지대, 0 이면 보류, 1이면 위험지대

    count = 0

    for j in range(y+1,N):
        top = max(x-(j-y),0)
        bottom = min(x+(j-y),N-1)

        for i in range(top,bottom+1):
            
            if sight_grid[i][j] == 2:
                continue

            sight_grid[i][j] = 1

            for w in range(M):

                if warriors_status[w] != -1 and warriors[w][0] == i and warriors[w][1] == j: # 시야에 전사가 있는 경우
                    if not isTest:
                        warriors_status[w] = 1 # 석화시키기
                    count += 1

                    if i < x: # 위 대각선
                        for k in range(j+1,N):
                            top = max(i-(k-j),0)
                            bottom = i

                            for d in range(top, bottom+1):
                                sight_grid[d][k] = 2

                    elif i == x: # 오른쪽
                        for k in range(j+1,N):
                            sight_grid[i][k] = 2
                    
                    elif i > x : # 아래 대각선
                        for k in range(j+1,N):
                            top = i
                            bottom = min(i+(k-j),N-1)

                            for d in range(top, bottom+1):
                                sight_grid[d][k] = 2

    if not isTest:
        current_sight_grid = sight_grid
    return count

sight_list = [sight_up, sight_down, sight_left, sight_right]

distance = compute_distance(px,py,area)

if distance[mx][my] == -1:
    print(-1)
    sys.exit()

cx, cy = mx, my

while True:

    for w in range(M):
        if warriors_status[w] == 1:
            warriors_status[w] = 0
    
    # 1. 메두사의 이동
    for i in range(4):
        nx, ny = cx + dx[i], cy + dy[i]

        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue

        if distance[nx][ny] < distance[cx][cy]:
            cx, cy = nx, ny
            break
    
    # 메두사가 공원에 도착하는 턴에는 0을 출력하고 프로그램을 종료
    if cx == px and cy == py:
        print(0)
        break

    # 메두사가 이동한 칸에 전사가 있을 경우 전사는 사라진다.
    for i in range(M):
        if warriors[i][0] == cx and warriors[i][1] == cy:
            warriors_status[i] = -1

    sight, sight_count = -1, -1 # 방향, [메두사로 인해 돌이 된 전사의 수]

    for i,func in enumerate(sight_list): # 메두사는 상/하/좌/우 중 전사를 가장 많이 볼 수 있는 방향을 바라본다.
        temp_count = func(cx,cy,True)
        if temp_count > sight_count:
            sight_count = temp_count
            sight = i
    
    # 2. 메두사의 시선 공격
    sight_list[sight](cx,cy,False) 

    move_count = 0 # [모든 전사가 이동한 거리의 합]
    attack_count = 0 # [메두사를 공격한 전사의 수]

    distance_w = compute_distance_w(cx,cy)

    # 3. 전사들의 이동
    for w in range(M):
        wx, wy = warriors[w][0], warriors[w][1]
        status = warriors_status[w]

        if status == -1 or status == 1: # 사망 또는 석화인 경우
            continue

        for i in range(4):
            nwx, nwy = wx + dx[i], wy + dy[i]

            if nwx < 0 or nwx >= N or nwy < 0 or nwy >= N:
                continue

            if current_sight_grid[nwx][nwy] == 1:
                continue

            if distance_w[nwx][nwy] < distance_w[wx][wy]:
                wx, wy = nwx, nwy
                warriors[w][0], warriors[w][1] = wx, wy
                move_count += 1
                break

        # 4. 전사의 공격
        # 메두사와 같은 칸에 도달한 전사는 사라진다.
        if wx == cx and wy == cy:
            warriors_status[w] = -1
            attack_count += 1
            continue
        
        for i in range(4):
            nwx, nwy = wx + dx2[i], wy + dy2[i]

            if nwx < 0 or nwx >= N or nwy < 0 or nwy >= N:
                continue

            if current_sight_grid[nwx][nwy] == 1:
                continue

            if distance_w[nwx][nwy] < distance_w[wx][wy]:
                wx, wy = nwx, nwy
                warriors[w][0], warriors[w][1] = wx, wy
                move_count += 1
                break

        # 메두사와 같은 칸에 도달한 전사는 사라진다.
        if wx == cx and wy == cy:
            warriors_status[w] = -1
            attack_count += 1
    
    print(f"{move_count} {sight_count} {attack_count}")