N = int(input())

area = [[i * N + j for j in range(N)] for i in range(N)]

for row in area:
    print(row)

def rotate90_right():
    
    global area
    
    new_area = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            new_area[j][N-1-i] = area[i][j]

    area = new_area

def rotate90_left():

    global area

    new_area = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            new_area[N-1-j][i] = area[i][j]

    area = new_area

rotate90_right()

rotate90_left()

for row in area:
    print(row)