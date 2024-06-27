import sys
from collections import deque

input = sys.stdin.readline

# 아침에 출근해보면 테스트 차량들 위에 눈얼음이 생겨있음
# 커다란 얼음이 녹고난 뒤에 테스트가 가능
# 차량마다 당일의 테스트 가능 시점을 알기 위한 예측 프로그램 제작

# N x M 크기의 격자 위에 눈 얼음의 모양을 작은 정사각형들이 집합되어 있는 모양으로 변환
# 아침이 되면 기온이 상승하여 천천히 녹는다

# 얼음은 상하좌우 중에서 적어도 2변 이상이 외부와 접촉했을 때 정확히 1시간만에 녹음
# 얼음 내부에 있는 공간은 얼음 외부 공기와 접촉하지 않는 걸로 가정

# 주어진 얼음이 모두 녹아서 사라지는데 걸리는 시간

n, m = map(int,input().split())

area = [list(map(int,input().split())) for _ in range(n)]

dx, dy = [-1,1,0,0], [0,0,-1,1]


time = 0

def check_all_malt():
    for i in range(n):
        for j in range(m):
            if area[i][j] == 1:
                return False
    return True

def bfs():

    visited = [[0]*m for _ in range(n)]

    queue = deque([(0,0)])
    visited[0][0] = True

    while queue:
        x, y = queue.popleft()

        visited[x][y] = -1

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:

                if area[nx][ny] == 1:
                    visited[nx][ny] += 1
                elif area[nx][ny] == 0 and visited[nx][ny] != -1:
                    visited[nx][ny] = -1
                    queue.append((nx,ny))
                    
    for i in range(n):
        for j in range(m):
            if visited[i][j] >= 2:
                area[i][j] = 0
                    
while True:
    if check_all_malt():
        break
        
    time += 1
    bfs()

print(time)