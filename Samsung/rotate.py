N = int(input())

area = [[i * N + j for j in range(N)] for i in range(N)]

for row in area:
    print(row)

print()

def rotate90_right():
    
    global area
    
    new_area = [[0]*N for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            new_area[j][N-i-1] = area[i][j]

    return new_area

area = rotate90_right()

for row in area:
    print(row)
print()

def rotate90_left():
    
    new_area = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            new_area[N-j-1][i] = area[i][j]
    
    return new_area

area = rotate90_left()

for row in area:
    print(row)