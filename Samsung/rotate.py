# N = int(input())

# area = [[i * N + j for j in range(N)] for i in range(N)]

# for row in area:
#     print(row)

# print()

# def rotate90(arr):

#     N = len(arr)
    
#     new_area = [[0]*N for _ in range(N)]

#     for i in range(N):
#         for j in range(N):
#             new_area[j][N-1-i] = arr[i][j]

#     return new_area

# area = rotate90(area)

# for row in area:
#     print(row)
# print()

# def rotate180(arr):
    
#     N = len(arr)

#     new_area = [[0]*N for _ in range(N)]

#     for i in range(N):
#         for j in range(N):
#             new_area[N-1-i][N-1-j] = area[i][j]

#     return new_area

# area = rotate180(area)

# for row in area:
#     print(row)
# print()

# def rotate270(arr):

#     N = len(arr)

#     new_area = [[0]*N for _ in range(N)]

#     for i in range(N):
#         for j in range(N):
#             new_area[N-1-j][i] = arr[i][j]

#     return new_area

# area = rotate270(area)

# for row in area:
#     print(row)

def rotate90(arr):

    N = len(arr)
    
    new_area = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            new_area[j][N-1-i] = arr[i][j]

    return new_area
def partial_rotate90(area,x,y,d):

    N = len(area)

    new_area = [x[:] for x in area]

    for i in range(d):
        for j in range(d):
            new_area[x+j][y+d-1-i] = area[x+i][y+j]

    for i in new_area:
        print(i)

test = [[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 10, 11, 12],
[13, 14, 15, 16]]

partial_rotate90(test,1,1,2)