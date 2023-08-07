from collections import deque
n = int(input())
k = int(input())

area = [[0]*n for _ in range(n)]
direction_list = []

time = 0

for _ in range(k):
    r,c = map(int,input().split())
    area[r-1][c-1] = 1

l = int(input())

for _ in range(l):
    x, c = input().split()
    direction_list.append((int(x),c))

x, y = 0, 0

direction = "R"

tail = deque([(0,0)])

index = 0

while 1:
    
    area[x][y] = -1

    if time == direction_list[index][0]: # index에 해당하는 시간이 지났을 경우

        if direction_list[index][1] == "L": # 왼쪽으로 회전
            if direction == "R":
                direction = "U"
            elif direction == "L":
                direction = "D"
            elif direction == "U":
                direction = "L"
            elif direction == "D":
                direction = "R"

        elif direction_list[index][1] == "D": # 오른쪽으로 회전
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
    
    # 방향에 따른 다음 위치 설정
    if direction == "R":
        nx, ny = x, y + 1
    elif direction == "L":
        nx, ny = x, y - 1
    elif direction == "U":
        nx, ny = x - 1, y
    elif direction == "D":
        nx, ny = x + 1, y

    # 벽에 부딪히거나 자기자신의 몸과 부딪힌 경우 게임종료
    if nx < 0 or nx >= n or ny < 0 or ny >= n or area[nx][ny] == -1:
        time += 1
        break

    if tail and area[nx][ny] == 0: # 이동한 칸에 사과가 없는 경우
        tail_x, tail_y = tail.popleft()
        area[tail_x][tail_y] = 0 # 꼬리 비워주기

    tail.append((nx,ny))

    x = nx
    y = ny
    time += 1

print(time)