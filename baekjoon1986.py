from collections import deque

n, m = map(int,input().split())

# Knight, Queen, Pawn의 개수는 각각 100을 넘지 않는 음이 아닌 정수
queen_list = list(map(int,input().split()))
knight_list = list(map(int,input().split()))
pawn_list = list(map(int,input().split()))

# Queen은 가로,세로,대각선으로 이동 가능 / 장애물 통과 X
# Knight는 2x3 직사각형의 반대쪽 꼭짓점으로 이동 가능 / 장애물 통과 O

queen_count = queen_list.pop(0)
knight_count = knight_list.pop(0)
pawn_count = pawn_list.pop(0)

dx = [-1,1,0,0,-1,1,-1,1]
dy = [0,0,-1,1,-1,1,1,-1]

k_dx = [-1,-2,-2,-1,1,1,2,2]
k_dy = [-2,-1,1,2,-2,2,-1,1]

queen_list = [(x,y) for x,y in zip(queen_list[0::2], queen_list[1::2])]
knight_list = [(x,y) for x,y in zip(knight_list[0::2], knight_list[1::2])]
pawn_list = [(x,y) for x,y in zip(pawn_list[0::2], pawn_list[1::2])]

area = [[0]*m for _ in range(n)]

answer = 0

for pawn_x,pawn_y in pawn_list:
    area[pawn_x-1][pawn_y-1] = -1

for queen_x, queen_y in queen_list:
    area[queen_x-1][queen_y-1] = -1

for knight_x, knight_y in knight_list:
    area[knight_x-1][knight_y-1] = -1


def queen_move(x,y): # 퀸 이동 함수

    for i in range(8):
        nx, ny = x, y

        while 0 <= nx < n and 0 <= ny < m:
            nx = nx + dx[i]
            ny = ny + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if area[nx][ny] == -1: # 처음에 틀렸던 부분(어떤 퀸이 어떤 칸에 먼저 방문했다고 해서, 다른 퀸이 그 칸을 지나가면 안 되는 건 아니다.)
                    break
                area[nx][ny] = 1

def knight_move(x,y): # 나이트 이동 함수

    for i in range(8):
        nx = x + k_dx[i]
        ny = y + k_dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            area[nx][ny] = 1

    if is_exist(nx,ny):
        return nx,ny
    else:
        return -1,-1

def is_exist(x,y): # 해당 좌표에서 나이트가 이동할 경로가 있는지 확인하는 함수
    is_exist = False
    for i in range(8):
        nx = x + k_dx[i]
        ny = y + k_dy[i]
        if 0 <= nx < n and 0 <= ny < m and area[nx][ny] == 0:
            is_exist = True
    return is_exist

for queen_x,queen_y in queen_list: # 퀸 이동
    queen_move(queen_x-1,queen_y-1)

queue = deque(knight_list)

while queue: # 더이상 이동할 나이트가 없을 때까지 진행
    knight_x, knight_y = queue.popleft()

    result_x,result_y = knight_move(knight_x-1,knight_y-1)

    if not result_x == -1 and result_y == -1:
        queue.append((result_x,result_y))

for i in range(n):
    for j in range(m):
        if area[i][j] == 0:
            answer += 1

print(answer)
        
