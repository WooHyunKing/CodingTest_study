# 각 칸은 빈칸, 함정, 벽으로 구성 (체스판 밖도 벽으로 간주)
# 기사들은 상대방을 밀쳐낼 수 있다.
# 기사들의 초기 위치는 좌측 상단 (r,c)부터 h x w 크기의 직사각형 형태를 띔
# 기사들의 초기 체력은 k

# 1) 기사의 이동
# 상하좌우 중 하나로 이동
# 이동하려는 위치에 기사가 있다면 연쇄적으로 1칸씩 밀리게 됨
# 하지만 기사가 이동하려는 방향의 끝에 벽이 있다면 모든 기사는 이동 X

# 또한, 체스판에서 사라진 기사에게 명령을 내리면 반응 X

# 2) 대결 데미지
# 명령을 받은 기사가 다른 기사를 밀치게 되면 밀려난 기사들은 피해를 입는다.
# 각 기사들은 해당 기사가 이동한 위치에서 w x h 직사각형 내에 놓여있는 함정의 수 만큼 피해를 입는다.
# 각 기사들은 현재 체력 이상의 데미지를 받을 경우 체스판에서 사라진다.(사망)
# 단, 명령을 받은 기사는 피해를 입지 않으며 기사들은 모두 밀린 이후에 데미지를 입게 된다.

# Q번의 명령이 주어지고, 대결이 모두 끝난 후 [생존한 기사들이 총 받은 데미지의 합]을 구하라.

import sys

from collections import deque

input = sys.stdin.readline

L, N, Q = map(int,input().split())

dx, dy = [-1,0,1,0], [0,1,0,-1]

# 빈칸 - 0, 함정 - 1, 벽 - 2
area = [list(map(int,input().split())) for _ in range(L)]

warriors = [[]]

warriors_copy = [[]]

warriors_dict = dict()

boom_set = set()

wall_set = set()

for i in range(1,N+1):

    r,c,h,w,k = map(int,input().split())

    r -= 1
    c -= 1

    warriors.append([r,c,h,w,k])
    warriors_copy.append([r,c,h,w,k])
    
    warriors_dict[i] = set()

    for n in range(h):
        for m in range(w):
            warriors_dict[i].add((r+n, c+m))

for i in range(L):
    for j in range(L):
        if area[i][j] == 1:
            boom_set.add((i,j))
        elif area[i][j] == 2:
            wall_set.add((i,j))


# 상 - 0, 우 - 1, 하 - 2, 좌 - 3
commands = [list(map(int,input().split())) for _ in range(Q)]


for wi, di in commands:
    
    cx, cy, ch, cw, hp = warriors[wi]

    # 체스판에서 사라진 기사에게 명령을 내리면 반응 X
    if hp <= 0:
        continue

    next_coors = set([(x+dx[di], y+dy[di]) for x,y in warriors_dict[wi]] )

    if len(next_coors & wall_set) >= 1:
        continue

    next_warriors = deque([])

    for i in range(1,N+1):
        
        # 같은 기사면 Pass
        if i == wi:
            continue
        # 80% 실패, 테스트케이스 38번(이미 사라진 기사는 반응하지 않는다.)
        if warriors[i][4] <= 0:
            continue
        
        temp_coors = warriors_dict[i]

        if len(next_coors & temp_coors) >= 1:
            next_warriors.append(i)

    temp_warriors_dict = dict()
    total_next_coors = next_coors

    all_warriors = set(next_warriors)

    while next_warriors:
        next_w = next_warriors.popleft()
        temp_coor_set = warriors_dict[next_w]
        temp_coor_set = set([(x+dx[di], y+dy[di]) for x, y in temp_coor_set])

        temp_warriors_dict[next_w] = temp_coor_set

        total_next_coors |= temp_coor_set

        for i in range(1,N+1):

            if i == wi:
                continue
            if i in all_warriors:
                continue
            # 80% 실패, 테스트케이스 38번(이미 사라진 기사는 반응하지 않는다.)
            if warriors[i][4] <= 0:
                continue

            temp_coors = warriors_dict[i]

            if len(total_next_coors & temp_coors) >= 1:
                next_warriors.append(i)
                all_warriors.add(i)

    is_available = True

    for x, y in total_next_coors:

        # 체스판 밖으로 넘어간 경우
        if x < 0 or y < 0 or x >= L or y >= L:
            is_available = False
            break
            
        # 기사가 이동하려는 방향의 끝에 벽이 있는 경우
        if area[x][y] == 2:
            is_available = False
            break
    
    if is_available:
        
        for next_w in all_warriors:
            warriors_dict[next_w] = temp_warriors_dict[next_w]

        current_coor_set = set([(tx+dx[di], ty+dy[di]) for tx,ty in warriors_dict[wi]])

        warriors_dict[wi] = current_coor_set
    
    else:
        continue

        
    for i in all_warriors:

        boom_count = len(warriors_dict[i] & boom_set)
        
        warriors[i][4] -= boom_count


result = 0

for i in range(1,N+1):
    if warriors[i][4] > 0:
        result += abs(warriors_copy[i][4] - warriors[i][4])

print(result)