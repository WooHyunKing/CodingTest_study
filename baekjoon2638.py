import sys
from collections import deque

input = sys.stdin.readline

dx, dy = [-1,1,0,0], [0,0,-1,1]

# 치즈는 실내온도에 내어놓으면 공기와 접촉하여 천천히 녹는다
# 각 치즈 격자(작은 정사각형 모양)의 4변 중에서 적어도 2변 이상이 실내온도의 공기와 접촉한 것은 정확히 한시간만에 녹아 없어져 버린다

N, M = map(int,input().split())

# 치즈가 있는 부분은 1로 표시되고, 치즈가 없는 부분은 0으로 표시
# 모눈종이의 맨 가장자리에는 치즈가 놓이지 않는 것으로 가정

# 출력 : 입력으로 주어진 치즈가 모두 녹아 없어지는데 걸리는 정확한 시간

area = [list(map(int,input().split())) for _ in range(N)]

answer = 0

def bfs():
    
    visited = [[False]*M for _ in range(N)]
    count = [[0]*M for _ in range(N)]

    q = deque([(0,0)])
    visited[0][0] = True

    while q:
        cx, cy = q.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if area[nx][ny] == 1:
                    count[nx][ny] += 1
                else:
                    if not visited[nx][ny]:
                        q.append((nx,ny))
                        visited[nx][ny] = True
    for i in range(N):
        for j in range(M):
            if count[i][j] >= 2:
                area[i][j] = 0

def check_empty():
    
    if sum([sum(x) for x in area]) == 0:
        return True
    else:
        return False

while not check_empty():

    answer += 1
    bfs()

print(answer)