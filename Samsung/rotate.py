N = int(input())

area = [[i * N + j for j in range(N)] for i in range(N)]

for row in area:
    print(row)

print()

def rotate90(arr):

    N = len(arr)
    
    new_area = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            new_area[j][N-1-i] = arr[i][j]

    return new_area

area = rotate90(area)

for row in area:
    print(row)
print()

def rotate180(arr):
    
    N = len(arr)

    new_area = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            new_area[N-1-i][N-1-j] = area[i][j]

    return new_area

area = rotate180(area)

for row in area:
    print(row)
print()

def rotate270(arr):

    N = len(arr)

    new_area = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            new_area[N-1-j][i] = arr[i][j]

    return new_area

area = rotate270(area)

for row in area:
    print(row)