from collections import deque
import math
N, L ,R = map(int,input().split())

data = [list(map(int,input().split())) for _ in range(N)]

visited = [[False]*N for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

count = 0

def bfs(x,y): # 국경선을 열고 인구를 이동시키는 BFS 함수
    if visited[x][y]: # 이미 방문한 곳이면 Pass
        return False

    visited[x][y] = True
    group = [(x,y)] # 연합을 이룬 좌표 목록
    total = data[x][y] # 연합의 총합

    queue = deque([(x,y)])

    while queue:
        temp_x, temp_y = queue.popleft()
        for i in range(4):
            nx = temp_x + dx[i]
            ny = temp_y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if L <= abs(data[temp_x][temp_y]-data[nx][ny]) <= R:
                    queue.append((nx,ny))
                    visited[nx][ny] = True
                    group.append((nx,ny)) # 연합에 추가
                    total += data[nx][ny] # 연합의 총합에 더하기

    if len(group) > 1: # 연합을 이루었을 경우 인구수 조정한 후 True 반환
        average = math.trunc(total / len(group))
    
        for group_x,group_y in group:
            data[group_x][group_y] = average

        return True
    else: # 연합을 이루지 못하였을 경우 False 반환
        return False

def check(): # 인구 이동이 있었는지 확인하는 함수
    is_moved = False

    for i in range(N):
        for j in range(N):
            if bfs(i,j): # bfs 함수가 True를 반환하면 인구 이동이 있었다고 판단
                is_moved = True

    return is_moved

while 1:
    if not check(): # 인구 이동이 발생하지 않았다면 무한루프 탈출
        break
    else: # 인구 이동이 발생했다면 +1 카운팅
        count += 1
	
    visited = [[False]*N for _ in range(N)] # 새로운 인구 이동을 위해 방문여부 배열 초기화

print(count)