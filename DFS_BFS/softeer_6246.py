import sys
from collections import deque

# 0 - 빈칸, 1 - 벽

# 이동은 상하좌우 중 인접한 칸만 가능
# 한번 지났던 지점은 다시 방문 X
# 방문해야 하는 지점의 첫 지점이 출발점, 마지막 지점이 도착점

# 순서대로 방문해야 하는 칸을 이동하는 시나리오 수

input = sys.stdin.readline

n, m = map(int,input().split())

area = [list(map(int,input().split())) for _ in range(n)]

visited = [[False]*n for _ in range(n)]

visit_list = [] # 방문해야 하는 지점들을 저장하는 배열

answer = 0

dx, dy = [-1,1,0,0], [0,0,-1,1]

for _ in range(m):
    vx, vy = map(int,input().split())
    visit_list.append((vx-1,vy-1))
    
queue = deque(visit_list) # 앞으로 방문해야 하는 지점들을 저장하는 배열

def dfs(x,y):

    global answer

    is_poped = False # 현재 위치가 방문해야 하는 지점인지 저장하는 Boolean값

    if queue and queue[0] == (x,y): # 현재 위치가 방문해야 하는 위치라면
        is_poped = True 
        poped_x_and_y = queue.popleft() # 앞으로 방문해야 하는 지점 Update (방문한 지점은 제거, 순서대로 이루어져야 하므로 큐 사용)

    if x == visit_list[-1][0] and y == visit_list[-1][1]: # 도착 지점일 경우
        if len(queue) == 0: # 이전에 방문해야 할 지점들을 모두 방문했다면 카운트 + 1
            answer += 1 
        return True # 더 이상 탐색하지 않기 위해 Return
    
    visited[x][y] = True # 방문처리

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and area[nx][ny] == 0:
            dfs(nx,ny)
    
    visited[x][y] = False # 원상복구를 위한 방문처리 취소
    
    if is_poped: # 원상복구를 위한 큐 데이터 삽입
        queue.appendleft(poped_x_and_y)

dfs(visit_list[0][0], visit_list[0][1]) # 출발지점부터 DFS 탐색 시작
    
print(answer)