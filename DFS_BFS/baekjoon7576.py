from collections import deque

# 가로(m), 세로(n)
m, n = map(int,input().split())

# 토마토가 담긴 상자(2차원 리스트)
area = []
# 토마토가 존재하는 위치를 담는 리스트
exist_list = []

# 토마도가 모두 익는 최소 일수(정답)
result = 0

# BFS 함수
def bfs(list):

  global result

  queue = deque(list)
    
  # 익을 수 있는 토마토가 다 익었을 때, 마지막 구역에 저장된 값
  depth = 0

  while queue:

    v = queue.popleft()

    nx = [-1,1,0,0]
    ny = [0,0,-1,1]

    for i in range(4):
      temp_x = v[0] + nx[i]
      temp_y = v[1] + ny[i]

      # 배열의 영역을 벗어났는지 / 다음 영역에 익지 않은 토마토가 있는지 확인
      if temp_x >=0 and temp_x < n and temp_y >= 0 and temp_y <m and area[temp_x][temp_y] == 0:
        # 조건을 만족하면 (현재 값 + 1) 저장
        area[temp_x][temp_y] = area[v[0]][v[1]] + 1
        depth = area[v[0]][v[1]] + 1
        # 큐에 삽입
        queue.append((temp_x,temp_y))

  # 1에서 부터 시작했기 때문에 정답은 (depth - 1)
  result = depth -1

# 토마토 위치 정보 입력받기
for _ in range(n):
  area.append(list(map(int,input().split())))

# 만약에 처음부터 모든 토마토가 익어있는 상태라면 0 출력
if all(0 not in l for l in area):
  print(0)

else:
  for i in range(n):
    for j in range(m):
      if area[i][j] == 1:
        exist_list.append((i,j))

  bfs(exist_list)

  # 시간이 지나도 토마토가 익지 못하는 경우 -1 출력
  if any(0 in l for l in area):
    print(-1)
  
  else:
    print(result)