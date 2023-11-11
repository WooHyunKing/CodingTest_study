import sys

# 세로 h, 가로 w
h,w = map(int,input().split())

# 방문 '#', 방문X '.'
area = [list(input()) for _ in range(h)]

# '>', 'v', '<', '^'
dx = [0,1,0,-1]
dy = [1,0,-1,0]

# L : 왼쪽으로 90도 회전
# R : 오른쪽으로 90도 회전
# A : 바라보는 방향으로 2칸 전진

def turnLeft(index):
  # 0,0 -> 3,3
  if index == 0:
    return 3
  return index-1
def turnRight(index):
  # 0,0 -> 3,3
  if index == 3:
    return 0
  return index+1

def moveA(x,y,direct,area):
  if direct == "<":
    if x - 2 >= 0:
      area[x-2][y] = '#'
      area[x-1][y] = '#'
      return "<",area

def compareArea(area,area2):
  is_same = True
  
  for i in range(h):
    for j in range(w):
      if area[i][j] != area2[i][j]:
        return False
  return is_same


start_list = []

for i in range(h):
  for j in range(w):
    if area[i][j] == '#':
      start_list.append((i,j))
print(start_list)



  
  

for i in area:
  print(i)

