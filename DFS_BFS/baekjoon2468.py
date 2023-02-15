from collections import deque

# 2차원 배열의 행과 열 개수
n = int(input())

# 지역 높이 정보(2차원 배열)
area = []
visited = [[False]*n for _ in range(n)]

count_list = []

solution = 0

for _ in range(n):
  area.append(list(map(int,input().split())))

max_value = max(map(max,area))

def bfs(x,y,value):

  if visited[x][y] or (area[x][y]-value) <= 0:
    return False
  
  visited[x][y] = True

  queue = deque([(x,y)])

  while queue:

    v = queue.popleft()

    nx = [-1,1,0,0]
    ny = [0,0,-1,1]

    for i in range(4):
      temp_x = v[0] + nx[i]
      temp_y = v[1] + ny[i]

      if temp_x >= 0 and temp_x < n and temp_y >= 0 and temp_y < n:
        if (area[temp_x][temp_y] - value) > 0 and not visited[temp_x][temp_y]:
          queue.append((temp_x,temp_y))
          visited[temp_x][temp_y] = True

  return True

for i in range(max_value+1):

    count = 0

    for j in range(n):
      for k in range(n):
        if bfs(j,k,i):
          count += 1

    count_list.append(count)

    visited = [[False]*n for _ in range(n)]
  

print(max(count_list))