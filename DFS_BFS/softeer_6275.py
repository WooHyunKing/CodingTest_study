import sys

input = sys.stdin.readline

dx, dy = [-1,1,0,0], [0,0,-1,1]

# L : 왼쪽으로 90도 회전
# R : 오른쪽으로 90도 회전
# A : 로봇이 바라보는 방향으로 2칸 전진(범위를 벗어나면 수행X)

# 같은 칸을 2번 이상 방문하지 못하도록 명령
# 출발지점을 포함한 로봇이 방문한 모든 칸을 지도에 표시

# 로봇이 지도에 사수에 표시한 모든 칸들만을 방문하도록 조작
# 1. 처음 로봇을 어떤 칸에, 어떤 방향으로 두어야 하는가 ?
# 2. 이후 로봇에 어떤 명령어를 순서대로 입력해야 하는가 ?

# 입력하는 명령어의 개수를 최소화 했을때 [첫번째 로봇의 위치 좌표], [방향], [명령어]

h, w = map(int,input().split())

# 방문했다면 '#', 방문하지 않았다면 '.'
area = [list(input().rstrip()) for _ in range(h)]

start_list = []

command_count = float("inf")

for i in range(h):
    for j in range(w):
        if area[i][j] == '#':
            if 0 <= j-1 < w and area[i][j-1] == '#':   
                start_list.append((i,j,'<'))
            if 0 <= j+1 < w and area[i][j+1] == '#':
                start_list.append((i,j,'>'))
            if 0 <= i-1 < h and area[i-1][j] == '#':
                start_list.append((i,j,'^'))
            if 0 <= i+1 < h and area[i+1][j] == '#':
                start_list.append((i,j,'v'))

def check_all_visited(area): # 로봇이 모든 좌표에 방문했는지 확인하는 함수

    for i in range(h):
        for j in range(w):
            if area[i][j] == '#':
                return False
    return True

answer_x, answer_y, answer_d,answer_command = 0,0,'',''

def dfs(x,y,d,commands,first_x,first_y,first_d):

    global command_count
    global answer_x
    global answer_y
    global answer_d
    global answer_command

    area[x][y] = '.'

    if check_all_visited(area):

        length = len("".join(commands))

        if length < command_count:
            command_count = length
            answer_x, answer_y, answer_d = first_x, first_y, first_d
            answer_command = "".join(commands)
        return
    

    # 1) 왼쪽으로 돌고 2칸 전진
    # 2) 오른쪽으로 돌고 2칸 전진
    # 3) 왼쪽으로 두번 돌고 2칸 전진
    # 4) 현재 방향에서 2칸 전진

    if 0 <= y-2 < w and area[x][y-1] == '#' and area[x][y-2] == '#':

        area[x][y-1] = '.'
        area[x][y-2] = '.'

        if d == '<':
            dfs(x,y-2,'<',commands+["A"],first_x,first_y,first_d)
        elif d == '>':
            dfs(x,y-2,'<',commands+["L","L","A"],first_x,first_y,first_d)
        elif d == '^':
            dfs(x,y-2,'<',commands+["L","A"],first_x,first_y,first_d)
        elif d == 'v':
            dfs(x,y-2,'<',commands+["R","A"],first_x,first_y,first_d)

        area[x][y-1] = '#'
        area[x][y-2] = '#'

    if 0 <= y+2 < w and area[x][y+1] == '#' and area[x][y+2] == '#':
        area[x][y+1] = '.'
        area[x][y+2] = '.'

        if d == '>':
            dfs(x,y+2,'>',commands+["A"],first_x,first_y,first_d)
        elif d == '<':
            dfs(x,y+2,'>',commands+["L","L","A"],first_x,first_y,first_d)
        elif d == '^':
            dfs(x,y+2,'>',commands+["R","A"],first_x,first_y,first_d)
        elif d == 'v':
            dfs(x,y+2,'>',commands+["L","A"],first_x,first_y,first_d)
            
        area[x][y+1] = '#'
        area[x][y+2] = '#'

    if 0 <= x-2 < h and area[x-1][y] == '#' and area[x-2][y] == '#':

        area[x-1][y] = '.'
        area[x-2][y] = '.'

        if d == '^':
            dfs(x-2,y,'^',commands+["A"],first_x,first_y,first_d)

        elif d == 'v':
            dfs(x-2,y,'^',commands+["L","L","A"],first_x,first_y,first_d)

        elif d == '<':
            dfs(x-2,y,'^',commands+["R","A"],first_x,first_y,first_d)

        elif d == '>':
            dfs(x-2,y,'^',commands+["L","A"],first_x,first_y,first_d)

        area[x-1][y] = '#'
        area[x-2][y] = '#'

    if 0 <= x+2 < h and area[x+1][y] == '#' and area[x+2][y] == '#':

        area[x+1][y] = '.'
        area[x+2][y] = '.'

        if d == 'v':
            dfs(x+2,y,'v',commands+["A"],first_x,first_y,first_d)
        elif d == '^':
            dfs(x+2,y,'v',commands +["L","L","A"],first_x,first_y,first_d)
        elif d == '<':
            dfs(x+2,y,'v',commands +["L","A"],first_x,first_y,first_d)
        elif d == '>':
            dfs(x+2,y,'v',commands +["R","A"],first_x,first_y,first_d)
        
        area[x+1][y] = '#'
        area[x+2][y] = '#'
        
    area[x][y] = '#'

for sx, sy, sd in start_list:
    dfs(sx,sy,sd,[],sx,sy,sd)

print(answer_x+1,answer_y+1)

print(answer_d)

print(answer_command)