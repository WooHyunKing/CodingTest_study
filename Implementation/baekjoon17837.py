
# 다음 칸이 흰색인 경우 
# 칸이 이미 있는 경우에는 현재 말을 전부 위에 쌓는다

# 다음 칸이 빨간색인 경우
# 칸이 이미 았는 경우에는 말들을 거꾸로 바꿔서 쌓는다

# 다음 칸이 파란색인 경우 / 체스판을 벗어나는 경우
# 반대 방향으로 한칸 이동, 단 반대편도 파란색인 경우 방향만 바꾸고 가만히 있는다.
# if 양 방향 모두 파란색인 경우 : 무시

dx = [0,0,-1,1]
dy = [1,-1,0,0]

# 체스판 크기 n, 말의 개수 k
n, k = map(int,input().split())

# 0 : 흰색, 1 : 빨간색, 2: 파란색
area = [list(map(int,input().split())) for _ in range(n)]

user_area = [[[]]*n for _ in range(n)]

print(user_area)

# 행, 열, 이동 방향(0 : 오른쪽, 1 : 왼쪽, 2 : 위, 3 : 아래)
user_info = [list(map(int,input().split())) for _ in range(k)]

for i in range(k):
    user_info[i].append(0)

for i in user_info:
    print(i)

def check_end(): # 게임이 종료되는지 확인하는 함수
    for i in range(n):
        for j in range(n):
            if len(user_area[i][j]) >= 4:
                return True
    return False

for i,value in enumerate(user_info):
    user_area[value[0]-1][value[1]-1] = [[i+1,0]]

print(user_area)

while not check_end():

    temp_user_info = [[] for _ in range(k)]
    
    for i in range(k):
        x, y, direction,index = user_info[i][0]-1, user_info[i][1]-1, user_info[i][2] -1, user_info[i][3]
        
        nx = x + dx[direction]
        ny = y + dy[direction]

        if 0 <= nx < n and 0 <= ny < n: # 다음 칸이 범위 내에 있는 경우
            if area[nx][ny] == 0: # 다음 칸이 흰색
                if user_area[nx][ny]: # 이미 칸에 말이 있는 경우
                    temp_index = len(user_area[nx][ny])
                    temp_list 
                    user_area[nx][ny] += user_area[x][y][index:]
                    user_area[x][y] = user_area[x][y][:index+1]
                    temp_user_info.append([nx,ny,direction,temp_index])
                else: # 칸에 말이 없는 경우
                    user_area[nx][ny] += user_area[x][y][index:]
                    user_area[x][y] = user_area[x][y][:index+1]
                    temp_user_info.append([nx,ny,direction,0])

            elif area[nx][ny] == 1: # 다음 칸이 빨간색
                if user_area[nx][ny]: # 이미 칸에 말이 있는 경우
                    temp_index = len(user_area[nx][ny])

                    temp_list = user_area[x][y][index:]

                    for j in range(len(temp_list)):
                        user_area[nx][ny].append(temp_list[-(j+1)])
                    
                    temp_user_info.append([nx,ny,direction,temp_index+len(temp_list)])

                    
                    user_area[nx][ny] += (user_area[x][y][index:].reverse())
                    user_area[x][y] = user_area[x][y][:index+1]
                    temp_user_info.append([nx,ny,direction,temp_index])
                else: # 칸에 말이 없는 경우
                    user_area[nx][ny] += user_area[x][y][index:]
                    user_area[x][y] = user_area[x][y][:index+1]
                    temp_user_info.append([nx,ny,direction,0])


        