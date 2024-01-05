r,c,n = map(int,input().split())

area = [list(input()) for _ in range(r)]

flag = False

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(r): # 초기 상태에서 1초 지난 상태로 초기화
    for j in range(c):
        if area[i][j] == "O":
            area[i][j] = 2

for _ in range(n-1): # n-1초 간 3 ~ 4과정 반복
    for i in range(r): # 폭탄이 설치되어 있지 않은 모든 칸에 폭탄을 설치
        for j in range(c):
            if area[i][j] == ".": # 빈칸에는 폭탄설치
                area[i][j] = 3
            else: # 폭탄은 1초 시간 경과
                area[i][j] -= 1

    temp_area = [item[:] for item in area] # 값 덮어쓰기를 방지하기 위해 별도의 2차원 배열 사용
    
    for i in range(r): # 3초 전에 설치된 폭탄이 모두 폭발
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