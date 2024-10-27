import sys

input = sys.stdin.readline

# 상근이는 2차원 평면 위에서 움직일 수 있는 거북이 로봇을 하나 가지고 있다.
# L과 R명령을 내렸을 때, 로봇은 이동하지 않고, 방향만 바꾼다.

# 상근이는 자신의 컨트롤 프로그램으로 거북이가 이동한 영역을 계산
# 출력 : 거북이가 지나간 영역을 모두 포함할 수 있는 가장 작은 직사각형의 넓이

# 단, 거북이가 지나간 영역이 직사각형을 만들지 않는 경우도 있다.

# F : 한 눈금 앞으로
# B : 한 눈금 뒤로
# L : 왼쪽으로 90도 회전
# R : 오른쪽으로 90도 회전

# 거북이는 가장 처음에 (0, 0)에 있고, 북쪽을 쳐다보고 있다.

dx, dy = [-1,0,1,0], [0,1,0,-1]

T = int(input())

for _ in range(T):

    cx, cy = 501, 501

    direction = 0

    maximum_x, maximum_y = 501, 501
    minimum_x, minimum_y = 501, 501
    
    program = list(input().rstrip())

    for p in program:
        if p == 'F':
            cx, cy = cx + dx[direction], cy + dy[direction]
            if cx < minimum_x:
                minimum_x = cx
            if cx > maximum_x:
                maximum_x = cx
            if cy < minimum_y:
                minimum_y = cy
            if cy > maximum_y:
                maximum_y = cy

        elif p == 'B':
            if direction == 0:
                temp_direction = 2
            elif direction == 2:
                temp_direction = 0
            elif direction == 1:
                temp_direction = 3
            elif direction == 3:
                temp_direction = 1
            cx, cy = cx + dx[temp_direction], cy + dy[temp_direction]
            if cx < minimum_x:
                minimum_x = cx
            if cx > maximum_x:
                maximum_x = cx
            if cy < minimum_y:
                minimum_y = cy
            if cy > maximum_y:
                maximum_y = cy

        elif p == 'L':
            direction = (direction+3)%4
        elif p == 'R':
            direction = (direction+1)%4

    print(abs(maximum_x - minimum_x)*abs(maximum_y-minimum_y))