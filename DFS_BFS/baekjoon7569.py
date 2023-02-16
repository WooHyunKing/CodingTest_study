import sys
input = sys.stdin.readline
from collections import deque

# 가로(m), 세로(n), 높이(h)
m, n, h = map(int,input().split())

# 3차원 리스트 선언 및 초기화
area = [[[0]*m for _ in range(n)] for _ in range(h)]

# 3차원 리스트 입력받기
for i in range(h):
  for j in range(n):
    area[i][j] = list(map(int,input().split()))

# 값이 1인 인덱스(높이,세로,가로)배열
one_list = []
# 값이 0인 인덱스(높이,세로,가로)배열
zero_list = []

# 3차원 리스트에서 값이 1인 인덱스와 값이 0인 인덱스를 각 배열에 저장
for i in range(h):
  for j in range(n):
    for k in range(m):
      if area[i][j][k] == 1:
        one_list.append((i,j,k))
      elif area[i][j][k] == 0:
        zero_list.append((i,j,k))

# 만약에 처음부터 익지 않은 토마토가 없는 경우 0을 출력하고 종료
if len(zero_list) == 0:
  print(0)
  sys.exit()

# 정답(토마토가 최종적으로 다 익을 때까지 걸리는 최소 일수)
solution = 0

# BFS 함수
def bfs(one_list):

  global solution

  queue = deque([])

  # 먼저 익은 토마토(1)부터 큐에 삽입
  for i in one_list:
    if area[i[0]][i[1]][i[2]] <= 0:
      return False

    queue.append(i)

  # 큐가 비워질 때까지
  while queue:

    v = queue.popleft()

    # 상하좌우, 위, 아래 순회를 위한 값
    nx = [-1,1,0,0,0,0]
    ny = [0,0,-1,1,0,0]
    nz = [0,0,0,0,-1,1]

    # 상하좌우, 위, 아래를 탐색
    for i in range(6):
      temp_z = v[0] + nz[i]
      temp_x = v[1] + nx[i]
      temp_y = v[2] + ny[i]

      
      # 배열의 범위를 벗어나지 않는지 확인
      if temp_z >=0 and temp_z < h and temp_x >= 0 and temp_x < n and temp_y >= 0 and temp_y < m:
        # 익지 않은 토마토가 존재하는지 확인
        if area[temp_z][temp_x][temp_y] == 0:
          # 큐에 삽입
          queue.append((temp_z,temp_x,temp_y))
          # 다음 영역의 값은 현재 영역 + 1(하루가 지날 때 마다 카운팅)
          area[temp_z][temp_x][temp_y] = area[v[0]][v[1]][v[2]] + 1
          # 이동할 때 마다 최소 일수 업데이트
          solution = area[v[0]][v[1]][v[2]] + 1

# 익은 토마토(1)의 인덱스가 저장된 배열을 BFS 함수에 전달
bfs(one_list)

# 시간이 지나도 익지 못하는 토마토(0)이 존재하는 경우 -1을 출력하고 종료
for i in range(h):
  for j in range(n):
    for k in range(m):
      if area[i][j][k] == 0:
        print(-1)
        sys.exit()

# 최종적인 답은 걸린 일수이므로 -1 해주기
print(solution-1)