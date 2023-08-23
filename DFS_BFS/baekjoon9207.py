from collections import deque
n = int(input())

dx = [-1,1,0,0]
dy = [0,0,-1,1]

dx_2 = [-2,2,0,0]
dy_2 = [0,0,-2,2]

result = []

def move(movetime):

    global min_count, min_movement

    pin_list = []

    for i in range(5):
        for j in range(9):
            if area[i][j] == 'o':
                pin_list.append((i,j))

    if len(pin_list) < min_count:
        min_movement = movetime
        min_count = len(pin_list)

    for x,y in pin_list:
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            nx_2, ny_2 = x + dx_2[i], y + dy_2[i]
            if 0 <= nx < 5 and 0 <= ny < 9 and area[nx][ny]=='o' and 0 <= nx_2 < 5 and 0 <= ny_2 < 9 and area[nx_2][ny_2] == '.':
                area[nx_2][ny_2] = 'o'
                area[x][y] = '.'
                area[nx][ny] = '.'
                move(movetime+1)
                area[nx_2][ny_2] = '.'
                area[x][y] = 'o'
                area[nx][ny] = 'o'         

for i in range(n):
    min_count = 10
    min_movement = 10
    area = [list(input().rstrip()) for _ in range(5)]
    if i != n-1:
        input()
    move(0)
    result.append((min_count,min_movement))

for i in result:
    print(f'{i[0]} {i[1]}')