import sys
from collections import deque

input = sys.stdin.readline

# 가장 처음에 모든 칸의 온도는 0

# 1. 집에 있는 모든 온풍기에서 바람이 한 번 나옴
# 2. 온도가 조절됨
# 3. 온도가 1 이상인 가장 바깥쪽 칸의 온도가 1씩 감소
# 4. 초콜릿을 하나 먹는다.
# 5. 조사하는 모든 칸의 온도가 K 이상이 되었는지 검사. 
# 모든 칸의 온도가 K이상이면 테스트를 중단하고, 아니면 1부터 다시 시작한다.

# 온풍기에서 바람이 한 번 나왔을 때, 온풍기의 바람이 나오는 방향에 있는 칸은 항상 온도가 5도 올라간다.
# 그 다음 이 바람은 계속 다른 칸으로 이동해 다른 칸의 온도를 위의 그림과 같이 상승시키게 된다. 
# 어떤 칸 (x, y)에 온풍기 바람이 도착해 온도가 k (> 1)만큼 상승했다면, 
# (x-1, y+1), (x, y+1), (x+1, y+1)의 온도도 k-1만큼 상승하게 된다. 

# 이때 그 칸이 존하지 않는다면, 바람은 이동하지 않는다. 
# 온풍기에서 바람이 한 번 나왔을 때, 어떤 칸에 같은 온풍기에서 나온 바람이 여러 번 도착한다고 해도 온도는 여러번 상승하지 않는다.

# 일부 칸과 칸 사이에는 벽이 있어 온풍기 바람이 지나갈 수 없다. 

# 바람이 오른쪽으로 불었을 때 어떤 칸 (x, y)에서 (x-1, y+1)로 바람이 이동할 수 있으려면, (x, y)와 (x-1, y) 사이에 벽이 없어야 하고, (x-1, y)와 (x-1, y+1) 사이에도 벽이 없어야 한다. 
# (x, y)에서 (x, y+1)로 바람이 이동할 수 있으려면 (x, y)와 (x, y+1) 사이에 벽이 없어야 한다. 
# 마지막으로 (x, y)에서 (x+1, y+1)로 바람이 이동할 수 있으려면, (x, y)와 (x+1, y), (x+1, y)와 (x+1, y+1) 사이에 벽이 없어야 한다.

# 구사과의 집에는 온풍기가 2대 이상 있을 수도 있다. 이 경우 각각의 온풍기에 의해서 상승한 온도를 모두 합한 값이 해당 칸의 상승한 온도이다.

# 온풍기가 있는 칸도 다른 온풍기에 의해 온도가 상승할 수 있다.

R, C, K = map(int,input().split())

area = [list(map(int,input().split())) for _ in range(R)]

W = int(input())

wall_set = set()

execute_set = set()

check_set = set()

wall_dict = dict()

main_set = set()

visited_set = set()

continue_bool = True

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(W):
    x, y, t = map(int,input().split())
    wall_set.add((x-1,y-1,t))

for i, row in enumerate(area):
    for j, value in enumerate(row):
        if 1 <= value <= 4: # 온풍기인 경우
            execute_set.add((i,j,value))
            area[i][j] -= value
        elif value == 5:
            check_set.add((i,j))
            area[i][j] -= value            

def wind(x,y,d): # (x,y) 좌표에서 d 방향으로 바람을 불어 온도를 높이는 함수

    visited = [[False]*C for _ in range(R)]

    if d == 1: # 방향이 오른쪽인 온풍기
        
        if 0 <= y+1 < C:
            queue = deque([(x,y+1,5)])

        while queue:
            cx, cy, temp = queue.popleft()
            
            if not visited[cx][cy] and temp > 0: 
                area[cx][cy] += temp
                visited[cx][cy] = True
                if 0 <= cx-1 < R and 0 <= cy+1 < C and not visited[cx-1][cy+1] and (cx,cy,0) not in wall_set and (cx-1,cy,1) not in wall_set:
                    queue.append((cx-1,cy+1,temp-1))
                if 0 <= cx < R and 0 <= cy+1 < C and not visited[cx][cy+1] and (cx,cy,1) not in wall_set:
                    queue.append((cx,cy+1,temp-1))
                if 0 <= cx+1 < R and 0 <= cy+1 < C and not visited[cx+1][cy+1] and (cx+1,cy,0) not in wall_set and (cx+1,cy,1) not in wall_set:
                    queue.append((cx+1,cy+1,temp-1))
    elif d == 2: # 방향이 왼쪽인 온풍기
        if 0 <= y-1 < C:
            queue = deque([(x,y-1,5)])

        while queue:
            cx, cy, temp = queue.popleft()
            
            if not visited[cx][cy] and temp > 0: 
                area[cx][cy] += temp
                visited[cx][cy] = True
                if 0 <= cx-1 < R and 0 <= cy-1 < C and not visited[cx-1][cy-1] and (cx,cy,0) not in wall_set and (cx-1,cy-1,1) not in wall_set:
                    queue.append((cx-1,cy-1,temp-1))
                if 0 <= cx < R and 0 <= cy-1 < C and not visited[cx][cy-1] and (cx,cy-1,1) not in wall_set:
                    queue.append((cx,cy-1,temp-1))
                if 0 <= cx+1 < R and 0 <= cy-1 < C and not visited[cx+1][cy-1] and (cx+1,cy,0) not in wall_set and (cx+1,cy-1,1) not in wall_set:
                    queue.append((cx+1,cy-1,temp-1))
    elif d == 3: # 방향이 위쪽인 온풍기
        if 0 <= x-1 < R:
            queue = deque([(x-1,y,5)])

        while queue:
            cx, cy, temp = queue.popleft()
            
            if not visited[cx][cy] and temp > 0: 
                area[cx][cy] += temp
                visited[cx][cy] = True
                if 0 <= cx-1 < R and 0 <= cy-1 < C and not visited[cx-1][cy-1] and (cx,cy-1,0) not in wall_set and (cx,cy-1,1) not in wall_set:
                    queue.append((cx-1,cy-1,temp-1))
                if 0 <= cx-1 < R and 0 <= cy < C and not visited[cx-1][cy] and (cx,cy,0) not in wall_set:
                    queue.append((cx-1,cy,temp-1))
                if 0 <= cx-1 < R and 0 <= cy+1 < C and not visited[cx-1][cy+1] and (cx,cy+1,0) not in wall_set and (cx,cy,1) not in wall_set:
                    queue.append((cx-1,cy+1,temp-1))
    elif d == 4: # 방향이 아래쪽인 온풍기
        if 0 <= x+1 < R:
            queue = deque([(x+1,y,5)])

        while queue:
            cx, cy, temp = queue.popleft()
            
            if not visited[cx][cy] and temp > 0: 
                area[cx][cy] += temp
                visited[cx][cy] = True
                if 0 <= cx+1 < R and 0 <= cy-1 < C and not visited[cx+1][cy-1] and (cx+1,cy-1,0) not in wall_set and (cx,cy-1,1) not in wall_set:
                    queue.append((cx+1,cy-1,temp-1))
                if 0 <= cx+1 < R and 0 <= cy < C and not visited[cx+1][cy] and (cx+1,cy,0) not in wall_set:
                    queue.append((cx+1,cy,temp-1))
                if 0 <= cx+1 < R and 0 <= cy+1 < C and not visited[cx+1][cy+1] and (cx+1,cy+1,0) not in wall_set and (cx,cy,1) not in wall_set:
                    queue.append((cx+1,cy+1,temp-1))

def maintain(x,y): # (x,y) 좌표에서 사방으로 온도를 조절하는 함수

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < R and 0 <= ny < C and (x,y,nx,ny) not in visited_set:

            if i == 0 and (x,y,0) not in wall_set: # 위
                if area[x][y] > area[nx][ny]: # 현재 좌표보다 인접이 더 작은 경우
                    main_set.add((x,y,(abs(area[x][y]-area[nx][ny])//4),'minus',i))
                elif area[x][y] < area[nx][ny]: # 현재 좌표가 인접보다 더 작은 경우
                    main_set.add((x,y,(abs(area[x][y]-area[nx][ny])//4),'plus',i))
            elif i == 1 and (nx,ny,0) not in wall_set: # 아래
                if area[x][y] > area[nx][ny]: # 현재 좌표보다 인접이 더 작은 경우
                    main_set.add((x,y,(abs(area[x][y]-area[nx][ny])//4),'minus',i))
                elif area[x][y] < area[nx][ny]: # 현재 좌표가 인접보다 더 작은 경우
                    main_set.add((x,y,(abs(area[x][y]-area[nx][ny])//4),'plus',i))
            elif i == 2 and (nx,ny,1) not in wall_set: # 왼
                if area[x][y] > area[nx][ny]: # 현재 좌표보다 인접이 더 작은 경우
                    main_set.add((x,y,(abs(area[x][y]-area[nx][ny])//4),'minus',i))
                elif area[x][y] < area[nx][ny]: # 현재 좌표가 인접보다 더 작은 경우
                    main_set.add((x,y,(abs(area[x][y]-area[nx][ny])//4),'plus',i))
            elif i == 3 and (x,y,1) not in wall_set:
                if area[x][y] > area[nx][ny]: # 현재 좌표보다 인접이 더 작은 경우
                    main_set.add((x,y,(abs(area[x][y]-area[nx][ny])//4),'minus',i))
                elif area[x][y] < area[nx][ny]: # 현재 좌표가 인접보다 더 작은 경우
                    main_set.add((x,y,(abs(area[x][y]-area[nx][ny])//4),'plus',i))  

            visited_set.add((x,y,nx,ny))
            visited_set.add((nx,ny,x,y))

def decrease():

    for i in range(R):
        if area[i][0] > 0:
            area[i][0] -= 1
        if area[i][-1] > 0:
            area[i][-1] -= 1
    
    for i in range(1,C-1):
        if area[0][i] > 0:
            area[0][i] -= 1
        if area[-1][i] > 0:
            area[-1][i] -= 1

answer = 0

while continue_bool:

    if answer >= 100:
        answer = 101
        break

    for x, y, d in execute_set: # 1. 집에 있는 모든 온풍기에서 바람이 한 번 나옴
        wind(x,y,d)

    main_set = set()
    visited_set = set()
    
    for i in range(R): # 2. 온도 조절
        for j in range(C):
            maintain(i,j)

    for tx, ty, value, type, d in main_set:
        if type == 'plus':
            area[tx][ty] += value
            area[tx+dx[d]][ty+dy[d]] -= value
        elif type == 'minus':
            area[tx][ty] -= value
            area[tx+dx[d]][ty+dy[d]] += value
    
    decrease()

    answer += 1 # 4. 초콜릿을 하나 먹는다.

    temp = 0

    for cx, cy in check_set: # 5. 조사하는 모든 칸의 온도가 K 이상이 되었는지 검사. 모든 칸의 온도가 K이상이면 테스트를 중단하고, 아니면 1부터 다시 시작한다.
        if area[cx][cy] >= K:
            temp += 1

    if temp == len(check_set):
        continue_bool = False


print(answer)

    