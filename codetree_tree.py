# 제초제의 경우 k의 범위만큼 대각선으로 퍼지며, 
# 벽이 있는 경우 가로막혀서 전파되지 않습니다.

# 제초제가 뿌려진 칸에는 c년만큼 제초제가 남아있다가 c+1년째가 될 때 사라지게 됩니다.
# 제초제가 뿌려진 곳에 다시 제초제가 뿌려지는 경우에는 새로 뿌려진 해로부터 다시 c년동안 제초제가 유지

# 만약 박멸시키는 나무의 수가 동일한 칸이 있는 경우에는 행이 작은 순서대로, 
# 만약 행이 같은 경우에는 열이 작은 칸에 제초제를 뿌리게 됩니다.

# 각 3개의 과정이 1년에 걸쳐 진행된다고 했을 때, m년 동안 [총 박멸한 나무의 그루 수]를 구하는 프로그램

from collections import deque

import copy

# 격자의 크기 n, 박멸이 진행되는 년 수 m, 제초제의 확산 범위 k, 제초제가 남아있는 년 수 c
n, m, k, c = map(int,input().split())

# 빈 칸은 0, 벽은 -1, 제초제는 -2
area = [list(map(int,input().split())) for _ in range(n)]
delete_area = [[0]*n for _ in range(n)]

answer = 0

dx, dy, dx_2, dy_2 = [-1,1,0,0], [0,0,-1,1], [-1,-1,1,1], [-1,1,-1,1]

def grow_count(x,y): # (x,y)와 성장하는 값을 반환하는 함수

    count = 0

    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]

        if 0 <= nx < n and 0 <= ny < n and area[nx][ny] > 0:
            count += 1
    
    return (x,y,count)

# 1. 인접한 네 개의 칸 중 나무가 있는 칸의 수만큼 나무가 성장합니다. 성장은 모든 나무에게 동시에 일어납니다.
def grow(): 
    grow_set = set()

    for i in range(n):
        for j in range(n):
            if area[i][j] > 0:
                grow_set.add(grow_count(i,j))
    
    for gx, gy, value in grow_set:
        area[gx][gy] += value

def boom_count(x,y): # 번식되는 (x,y)와 성장하는 값, 번식시켜주는 (x,y)와 나무가 줄어드는 값
    
    empty_count = 0
    empty_list = []

    boom_list = []

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < n and 0 <= ny < n and area[nx][ny] == 0:
            empty_count += 1
            empty_list.append((nx,ny))

    if empty_count > 0:
        boom_value = (area[x][y] // empty_count)

        for ex, ey in empty_list:
            boom_list.append((ex,ey,boom_value))
    
    # boom_list.append((x,y,-(boom_value*empty_count)))

    return boom_list

# 2. 기존에 있었던 나무들은 인접한 4개의 칸 중 벽, 다른 나무, 제초제 모두 없는 칸에 번식을 진행합니다. 
# 이때 "각 칸의 나무 그루 수에서 총 번식이 가능한 칸의 개수만큼 나누어진 그루 수"만큼 번식
# 나눌 때 생기는 나머지는 버립니다. 번식의 과정은 모든 나무에서 동시에 일어나게 됩니다.
def boom(): # 2. 기존에 있었던 나무들은 인접한 4개의 칸 중 벽, 다른 나무, 제초제 모두 없는 칸에 번식을 진행

    boom_total_list = []
    for i in range(n):
        for j in range(n):
            if area[i][j] > 0:
                boom_total_list += boom_count(i,j)
    
    for bx, by, value in boom_total_list:
        area[bx][by] += value
# 3. 각 칸 중 제초제를 뿌렸을 때 나무가 가장 많이 박멸되는 칸에 제초제를 뿌립니다.
# 나무가 없는 칸에 제초제를 뿌리면 박멸되는 나무가 전혀 없는 상태로 끝
# 나무가 있는 칸에 제초제를 뿌리게 되면 4개의 대각선 방향으로 k칸만큼 전파
# 단 전파되는 도중 벽이 있거나 나무가 아예 없는 칸이 있는 경우, 
# 그 칸 까지는 제초제가 뿌려지며 그 이후의 칸으로는 제초제가 전파되지 않습니다. 

# 제초제가 뿌려진 칸에는 c년만큼 제초제가 남아있다가 c+1년째가 될 때 사라지게 됩니다. 
# 제초제가 뿌려진 곳에 다시 제초제가 뿌려지는 경우에는 새로 뿌려진 해로부터 다시 c년동안 제초제가 유지됩니다.

def delete_count(x,y): # (x,y)에 제초제를 뿌렸을 때 박멸되는 나무 수 반환

    count = 0

    queue = deque([])

    for i in range(4):
        nx, ny = x + dx_2[i], y + dy_2[i]

        if 0 <= nx < n and 0 <= ny < n:
            if area[nx][ny] > 0:
                count += area[nx][ny]
                queue.append((nx,ny,i,1))
            elif area[nx][ny] == -2:
                queue.append((nx,ny,i,1))

    while queue:
        temp_x, temp_y, d, length = queue.popleft()

        nx, ny = temp_x + dx_2[d], temp_y + dy_2[d]
        
        if 0 <= nx < n and 0 <= ny < n and length + 1 <= k and area[x][y]>0:

            if area[nx][ny] > 0:
                count += area[nx][ny]
                queue.append((nx,ny,d,length+1))
            elif area[nx][ny] == -2:
                queue.append((nx,ny,d,length+1))

    return (count + area[x][y],x,y)

def delete(): # 3. 각 칸 중 제초제를 뿌렸을 때 나무가 가장 많이 박멸되는 칸에 제초제를 뿌립니다.
    global answer

    delete_list = []
    for i in range(n):
        for j in range(n):
            if area[i][j] > 0:
                delete_list.append(delete_count(i,j))
    delete_list.sort(key = lambda x:(-x[0],x[1],x[2]))
    
    if not delete_list:
        return

    delete_value, delete_x, delete_y = delete_list[0]
    
    answer += delete_value

    queue = deque([])

    for i in range(4):
        nx, ny = delete_x + dx_2[i], delete_y + dy_2[i]

        if 0 <= nx < n and 0 <= ny < n:
            if area[nx][ny] > 0:
                area[nx][ny] = -2
                delete_area[nx][ny] = c+1
                queue.append((nx,ny,i,1))
            elif area[nx][ny] == 0:
                area[nx][ny] = -2
                delete_area[nx][ny] = c+1
            elif area[nx][ny] == -2:
                delete_area[nx][ny] = c+1    
                queue.append((nx,ny,i,1))   
    while queue:
        temp_x, temp_y, d, length = queue.popleft()

        nx, ny = temp_x + dx_2[d], temp_y + dy_2[d]

        if 0 <= nx < n and 0 <= ny < n and length + 1 <= k and area[nx][ny] == 0:
            area[nx][ny] = -2
            delete_area[nx][ny] = c+1
            queue.append((nx,ny,d,length+1))
        
        if 0 <= nx < n and 0 <= ny < n and length+1 <= k:
            if area[nx][ny] > 0:
                area[nx][ny] = -2
                delete_area[nx][ny] = c+1
                queue.append((nx,ny,d,length+1))
            elif area[nx][ny] == 0:
                area[nx][ny] = -2
                delete_area[nx][ny] = c+1
            elif area[nx][ny] == -2:
                delete_area[nx][ny] = c+1  
                queue.append((nx,ny,d,length+1))      
    area[delete_x][delete_y] = -2
    delete_area[delete_x][delete_y] = c+1


while m > 0:

    grow()

    boom()

    for i in range(n):
        for j in range(n):
            if delete_area[i][j] > 0:
                delete_area[i][j] -= 1
                if delete_area[i][j] == 0:
                    area[i][j] = 0

    delete()
    # for i in area:
    #     print(i)
    # print()

    m -= 1

print(answer)
