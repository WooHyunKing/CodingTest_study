N = int(input())

area = [[0]* N for _ in range(N)]

dx = [0,1,0,-1]
dy = [-1,0,1,0]

def spiral():
    x = y = N//2

    length = 1

    direction = movecount = n = 0

    while True:
        movecount += 1

        for _ in range(length):
            n += 1

            x += dx[direction]
            y += dy[direction]

            if  0 <= x < N and 0 <= y < N:
                area[x][y] = n
            else:
                return

        if movecount == 2:
            movecount = 0
            length += 1
        
        direction = (direction + 1)%4

spiral()

for i in area:
    print(i)

        

# def spin():

#     x = y = N//2

#     direction = 0

#     move_count = 0

#     number = 0

#     length = 1

#     while 0 <= x < N and 0 <= y < N:

#         move_count += 1

#         for _ in range(length):
#             nx = x + dx[direction]
#             ny = y + dy[direction]
            
#             number += 1
            
#             area[nx][ny] = number

#             x = nx
#             y = ny

#         if move_count == 2:
#             length += 1
#             move_count = 0

#         direction = (direction+1)%4

# spin()

# for row in area:
#     print(row)