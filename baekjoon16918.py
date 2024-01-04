r,c,n = map(int,input().split())

area = [list(input()) for _ in range(r)]

flag = False

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(r):
    for j in range(c):
        if area[i][j] == "O":
            area[i][j] = 2

for _ in range(n-1):
    for i in range(r):
        for j in range(c):
            if area[i][j] == ".":
                area[i][j] = 3
            else:
                area[i][j] -= 1
    temp_area = [item[:] for item in area]
    
    for i in range(r):
        for j in range(c):
            if area[i][j] != "." and area[i][j] <= 0:
                temp_area[i][j] = "."
                for k in range(4):
                    temp_x = i + dx[k]
                    temp_y = j + dy[k]
                        
                    if 0 <= temp_x < r and 0 <= temp_y < c:
                        temp_area[temp_x][temp_y] = "."
    area = temp_area

for i in range(r):
    for j in range(c):
        if area[i][j] != ".":
            area[i][j] = "O"

for i in range(r):
    print("".join(area[i]))