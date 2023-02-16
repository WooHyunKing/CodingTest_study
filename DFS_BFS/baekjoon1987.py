import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

from collections import deque
# 세로와 가로 칸 개수
r, c = map(int,input().split())

# 지나갔던 알파벳 정보 배열
alpha = [0]*26

result = 0

count_list = [[1]*c for _ in range(r)]

visited = [[False]*c for _ in range(r)]

area = [[0]*c for _ in range(r)]
for i in range(r):
  area[i] = (list(input()))

def dfs(x,y):

    global result

    if x < 0 or x >= r or y < 0 or y >= c or visited[x][y]:
        return False

    visited[x][y] = True

    alpha[ord(area[x][y])-65] = 1

    nx = [-1,1,0,0]
    ny = [0,0,-1,1]

    for i in range(4):
        temp_x = x + nx[i]
        temp_y = y + ny[i]
        
        if temp_x >= 0 and temp_x < r and temp_y >= 0 and temp_y < c:
            if not visited[temp_x][temp_y] and alpha[ord(area[temp_x][temp_y]) - 65] == 0:
                count_list[temp_x][temp_y] = count_list[x][y] + 1
                dfs(temp_x,temp_y)

    if count_list[x][y] > result:
      result = count_list[x][y]
    visited[x][y] = False
    alpha[ord(area[x][y])-65] = 0

dfs(0,0)
print(result)