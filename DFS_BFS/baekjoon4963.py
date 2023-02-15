count_list = []

def dfs(x,y,area,visited):

  if area[x][y] == 0 or visited[x][y]:
    return False

  visited[x][y] = True

  nx = [-1,1,-0,0,-1,-1,1,1]
  ny = [0,0,-1,1,-1,1,-1,1]

  for i in range(8):
    temp_x = x + nx[i]
    temp_y = y + ny[i]

    if temp_x >=0 and temp_x < n and temp_y >= 0 and temp_y < m:
      if not visited[temp_x][temp_y] and area[temp_x][temp_y] == 1:
        dfs(temp_x,temp_y,area,visited)

  return True

while True:
  m, n = map(int,input().split())

  count = 0

  if n == 0 and m == 0:
    break

  area = []
  visited = [[False]*m for _ in range(n)]

  for _ in range(n):
    area.append(list(map(int,input().split())))

  for i in range(n):
    for j in range(m):
      if dfs(i,j,area,visited):
        count += 1

  count_list.append(count)

for i in count_list:
  print(i)