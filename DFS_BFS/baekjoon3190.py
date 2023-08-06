from collections import deque
n = int(input())
k = int(input())

area = [[0]*n for _ in range(n)]
direction_list = []
direction_values = []

time = 0

for _ in range(k):
    r,c = map(int,input().split())
    area[r-1][c-1] = 1

l = int(input())

for _ in range(l):
    x, c = input().split()
    direction_list.append((int(x),c))

# print("list",direction_list)

x, y = 0, 0

direction = "R"

tail = deque([(0,0)])

index = 0

# for t, c in direction_list:
#     print("t,c : ",t,c)
#     print(direction)
#     for i in range(index,t):
#         direction_values.append(direction)
#     index = t
#     if c == "L": # 왼쪽으로 회전
#         if direction == "R":
#             direction = "U"
#         elif direction == "L":
#             direction = "D"
#         elif direction == "U":
#             direction = "L"
#         elif direction == "D":
#             direction = "R"
#     elif c == "D":
#         if direction == "R":
#             direction = "D"
#         elif direction == "L":
#             direction = "U"
#         elif direction == "U":
#             direction = "R"
#         elif direction == "D":
#             direction = "L"

# print("dir values",direction_values)

while 1:
    
    area[x][y] = -1
    # print(area)

    # for i in area:
    #     print(i)

    if time == direction_list[index][0]:
        # print("time, value",time,direction_list[index][0])
        if direction_list[index][1] == "L": # 왼쪽으로 회전
            if direction == "R":
                direction = "U"
            elif direction == "L":
                direction = "D"
            elif direction == "U":
                direction = "L"
            elif direction == "D":
                direction = "R"
        elif direction_list[index][1] == "D":
            if direction == "R":
                direction = "D"
            elif direction == "L":
                direction = "U"
            elif direction == "U":
                direction = "R"
            elif direction == "D":
                direction = "L"
        if index + 1 < len(direction_list):
            index += 1
        
    # current_direction = direction_values[time]
    
    if direction == "R":
        nx, ny = x, y + 1
    elif direction == "L":
        nx, ny = x, y - 1
    elif direction == "U":
        nx, ny = x - 1, y
    elif direction == "D":
        nx, ny = x + 1, y

    if nx < 0 or nx >= n or ny < 0 or ny >= n or area[nx][ny] == -1:
        # print(nx,ny)
        time += 1
        break

    if tail and area[nx][ny] == 0: # 이동한 칸에 사과가 없는 경우
        tail_x, tail_y = tail.popleft()
        # print("tail_x , tail_y : ",tail_x,tail_y)
        area[tail_x][tail_y] = 0 # 꼬리 비워주기

    tail.append((nx,ny))

    # print("nx,ny : ",nx,ny)
    x = nx
    y = ny
    time += 1


print(time)
    
    # -1 -1 -1 

        
        
    
    
