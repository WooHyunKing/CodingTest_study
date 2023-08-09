n,m = map(int,input().split())

r,c,d = map(int,input().split())

# 현재 방향을 기준으로 반시계방향으로 탐색
dx = [[0,1,0,-1],[-1,0,1,0],[0,-1,0,1],[1,0,-1,0]]
dy = [[-1,0,1,0],[0,-1,0,1], [1,0,-1,0],[0,1,0,-1]]

# 바라보는 방향이 북쪽인 경우
# dx_0 =[0,1,0,-1]
# dy_0 =[-1,0,1,0]

# 바라보는 방향이 동쪽인 경우
# dx_1 = [-1,0,1,0]
# dy_1 = [0,-1,0,1]

# 바라보는 방향이 남쪽인 경우
# dx_2 = [0,-1,0,1]
# dy_2 = [1,0,-1,0]

# 바라보는 방향이 서쪽인 경우
# dx_3 = [1,0,-1,0]
# dy_3 = [0,1,0,-1]

status = [list(map(int,input().split())) for _ in range(n)] # 방 상태
visited = [[False]*m for _ in range(n)] # 방문 여부

global count
count = 0

def dfs(x,y,direction):
    global count

    has_empty = False # 빈칸 존재 여부

    if not visited[x][y]: # 처음 방문했을 경우에만 방문 처리 및 카운팅
        visited[x][y] = True
        count += 1

    for i in range(4):
        nx = x + dx[direction][i]
        ny = y + dy[direction][i]
        
        if status[nx][ny] != 1 and not visited[nx][ny]: # 벽이 아니고 청소가 아직 이루어지지 않은 경우
            if dx[direction][i] == 0 and dy[direction][i] == 1:
                temp_d = 1
            elif dx[direction][i] == 0 and dy[direction][i] == -1:
                temp_d = 3
            elif dx[direction][i] == 1 and dy[direction][i] == 0:
                temp_d = 2
            elif dx[direction][i] == -1 and dy[direction][i] == 0:
                temp_d = 0
            has_empty = True
            dfs(nx,ny,temp_d)
            break # 로봇 청소기가 빈칸을 찾고 경로를 선택했기 때문에 탐색 중단

    if not has_empty: # 빈칸이 없는 경우
        opposite_direction = (direction+2)%4 # 후진 방향 설정
        opposite_x = x + dx[opposite_direction][3] # 후진한 x좌표
        opposite_y = y + dy[opposite_direction][3] # 후진한 y좌표
        
        if status[opposite_x][opposite_y] == 1: # 후진한 좌표가 벽일 경우 종료
            return
        else: # 벽이 아니라면 방향을 유지하면서 후진
            dfs(opposite_x,opposite_y,direction)

dfs(r,c,d)
print(count)