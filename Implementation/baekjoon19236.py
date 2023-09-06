import copy

def find_x_y(fish_number,area): # 물고기의 x,y 좌표를 찾는 함수
    for i in range(4):
        for j in range(4):
            if area[i][j][0] == fish_number:
                return i,j
            
def find_shark_loc(area): # 상어의 x,y 좌표를 찾는 함수
    for i in range(4):
        for j in range(4):
            if area[i][j][0] == -1:
                return i,j
            
def fish_move(x,y,area): # 해당 좌표에 위치한 물고기를 이동시키는 함수

    new_area = copy.deepcopy(area)

    value = new_area[x][y][0]
    d = new_area[x][y][1]
    
    temp_dx = dx[d:] + dx[:d]
    temp_dy = dy[d:] + dy[:d]

    for i in range(8):
        nx = x + temp_dx[i]
        ny = y + temp_dy[i]
        nd = (d+i)%8
        if 0 <= nx < 4 and 0 <= ny < 4 and new_area[nx][ny][0] != -1:
            if new_area[nx][ny][0] is None:
                new_area[nx][ny] = (value,nd)
                new_area[x][y] = (None,None)
            else:
                new_area[x][y] = (new_area[nx][ny][0], new_area[nx][ny][1])
                new_area[nx][ny] = (value,nd)

            break

    return new_area

def all_fish_move(area): # 모든 물고기들을 이동시키는 함수
    fish_list = []

    temp_area = copy.deepcopy(area)

    for i in range(4):
        for j in range(4):
            if area[i][j][0] != -1 and area[i][j][0] is not None:
                fish_list.append((area[i][j][0],area[i][j][1]))

    fish_list.sort(key=lambda x:x[0])

    for fish_num, direction in fish_list:
        start_fish_x, start_fish_y = find_x_y(fish_num,temp_area)
        temp_area = fish_move(start_fish_x,start_fish_y,temp_area)

    return temp_area

def get_shark_move_list(x,y,area): # 상어가 이동할 수 있는 좌표를 반환하는 함수
    
    value = area[x][y][0]
    d = area[x][y][1]
    
    move_list = []

    while 0 <= x < 4 and 0 <= y < 4:
        x += dx[d]
        y += dy[d]

        if 0 <= x < 4 and 0 <= y < 4 and area[x][y][0] is not None:
            move_list.append((x,y))
    
    return move_list

def shark_eat(shark_x,shark_y,fish_x,fish_y,area): # 상어가 주어진 좌표의 물고기를 잡아먹고 이동하는 함수
    temp = copy.deepcopy(area)
    ate_number = temp[fish_x][fish_y][0]
    temp[fish_x][fish_y] = (temp[shark_x][shark_y][0],temp[fish_x][fish_y][1])
    temp[shark_x][shark_y] = (None,None)
    
    return ate_number, temp

area = [[0]*4 for _ in range(4)]

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,-1,-1,-1,0,1,1,1]

for i in range(4):
    a1, b1, a2, b2, a3, b3, a4, b4 = map(int,input().split())

    area[i][0], area[i][1], area[i][2], area[i][3] = (a1,b1-1), (a2,b2-1), (a3,b3-1), (a4,b4-1)

answer = area[0][0][0] # 첫번째 물고기 번호에서 시작

area[0][0] = (-1,area[0][0][1]) # 상어는 0,0에서 시작하고, 방향은 유지


def dfs(area,total): # dfs함수

    global answer
    
    temp = all_fish_move(area)

    shark_loc_x, shark_loc_y = find_shark_loc(temp)
    
    shark_move_list = get_shark_move_list(shark_loc_x,shark_loc_y,temp)

    if len(shark_move_list) == 0: # 상어가 더이상 잡아먹을 물고기가 없을 경우 종료
        answer = max(answer,total)

    for next_x, next_y in shark_move_list:
        ate,temp2 = shark_eat(shark_loc_x,shark_loc_y,next_x,next_y,temp)
        dfs(temp2,total+ate)

dfs(area,answer)

print(answer)