n,m = map(int,input().split())

area = [list(map(int,input().split())) for _ in range(n)]

move_list = [] # 이동 정보 목록

for i in range(m):
    move_list.append(tuple(map(int,input().split())))

cloud_list= {(n-1,0), (n-1,1), (n-2,0), (n-2,1)} # 초기 구름 위치

dx = [0,-1, -1, -1, 0, 1, 1, 1] # 방향 x좌표
dy = [-1, -1, 0, 1, 1, 1, 0, -1] # 방향 y좌표

dx_2 = [-1,-1,1,1] # 대각선 이동을 위한 x좌표
dy_2 = [-1,1,-1,1] # 대각선 이동을 위한 y좌표

total = 0

def move(d,s): # 구름 이동 및 비 내리는 함수
    global cloud_list

    temp_list = set()
    
    for x,y in cloud_list:
        temp_x, temp_y = x+dx[d-1]*s, y+dy[d-1]*s
        temp_x = (temp_x % n + n) % n
        temp_y = (temp_y % n + n) % n
        area[temp_x][temp_y] += 1
        
        temp_list.add((temp_x, temp_y))
    
    cloud_list = temp_list

def waterCopy(): # 물 복사 버그 함수
    global cloud_list
    for x,y in cloud_list:
        for i in range(4):
            nx = x + dx_2[i]
            ny = y + dy_2[i]
            if 0 <= nx < n and 0 <= ny < n and area[nx][ny] > 0:
                area[x][y] += 1

def createNewCloud(): # 새로운 구름 생성 함수
    global cloud_list
    temp = set()
    for i in range(n):
        for j in range(n):
            if area[i][j] >= 2 and (i,j) not in cloud_list: # 문제 해결 코드(집합 자료형으로 in 연산 최적화)
                temp.add((i,j))
                area[i][j] -= 2
    cloud_list = temp

for temp_d,temp_s in move_list:
    move(temp_d,temp_s)
    waterCopy()
    createNewCloud()

for i in range(n):
    for j in range(n):
        total += area[i][j]

print(total)