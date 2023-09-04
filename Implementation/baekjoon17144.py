import sys

r, c, t = map(int, sys.stdin.readline().split())
area = [list(map(int, sys.stdin.readline().split())) for _ in range(r)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

cleaner_list = []

answer = 0

for i in range(r):
    for j in range(c):
        if area[i][j] == -1:
            cleaner_list.append(i)

def spread(area,x,y):
    spread_value = area[x][y] // 5

    spread_info = []
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < r and 0 <= ny < c and area[nx][ny] != -1:
            area[x][y] -= spread_value
            # area[nx][ny] += spread_value
            spread_info.append((nx,ny,spread_value))
    return spread_info

def move_left(down_row):
    temp = []
    
    for i in range(1,c):
        temp.append(area[down_row][i])
    for i in range(down_row-1,-1,-1):
        temp.append(area[i][-1])
    for i in range(c-2,-1,-1):
        temp.append(area[0][i])
    for i in range(1,down_row):
        temp.append(area[i][0])

    temp.insert(0,0)
    temp = temp[:-1]
    
    for i in range(1,c):
        area[down_row][i] = temp.pop(0)
    for i in range(down_row-1,-1,-1):
        area[i][c-1] = temp.pop(0)
    for i in range(c-2,-1,-1):
        area[0][i] = temp.pop(0)
    for i in range(1,down_row):
        area[i][0] = temp.pop(0)

def move_right(top_row):
    temp = []
    
    for i in range(1,c):
        temp.append(area[top_row][i])
    for i in range(top_row+1,r):
        temp.append(area[i][-1])
    for i in range(c-2,-1,-1):
        temp.append(area[r-1][i])
    for i in range(r-2,top_row,-1):
        temp.append(area[i][0])

    temp.insert(0,0)
    temp = temp[:-1]
    
    for i in range(1,c):
        area[top_row][i] = temp.pop(0)
    for i in range(top_row+1,r):
        area[i][-1] = temp.pop(0)
    for i in range(c-2,-1,-1):
        area[r-1][i] = temp.pop(0)
    for i in range(r-2,top_row,-1):
        area[i][0] = temp.pop(0)

for _ in range(t):

    spread_list = []

    for i in range(r):
        for j in range(c):
            if area[i][j] != 0 and area[i][j] != -1:
                spread_list += spread(area,i,j)

    for spread_x,spread_y,value in spread_list:
        area[spread_x][spread_y] += value

    move_left(cleaner_list[0])
    move_right(cleaner_list[1])

for i in range(r):
    for j in range(c):
        if area[i][j] != -1:
            answer += area[i][j]
            
print(answer)