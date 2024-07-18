import sys
from collections import deque
input = sys.stdin.readline

# 서 : 1
# 북 : 2
# 동 : 4
# 남 : 8

# 굵은 선은 벽을 나타내고, 점선은 벽이 없어서 지나다닐 수 있는 통로

# 1.성에 있는 방의 개수
# 2.가장 넓은 방의 넓이
# 3.하나의 벽을 제거하여 얻을 수 있는 가장 넓은 방의 크기

# 성에는 최소 두 개의 방이 있어서, 항상 하나의 벽을 제거하여 두 방을 합치는 경우가 있다.

dx, dy = [-1,1,0,0],[0,0,-1,1]

n, m = map(int,input().split())

visited = [[False]*n for _ in range(m)]

area = [list(map(int,input().split())) for _ in range(m)]

answer = []

maximum = float("-inf")

def get_block_info(n):

    return list(bin(n).split('0b')[1][::-1].ljust(4,'0'))

def bfs(x,y):

    if visited[x][y]:
        return -1
    
    visited[x][y] = True

    q = deque([(x,y)])

    count = 0

    while q:
        
        cx, cy = q.popleft()

        count += 1

        if 0 <= cx-1 < m and not visited[cx-1][cy] and get_block_info(area[cx][cy])[1] == '0':
            q.append((cx-1,cy))
            visited[cx-1][cy] = True
        if 0 <= cx+1 < m and not visited[cx+1][cy] and get_block_info(area[cx][cy])[3] == '0':
            q.append((cx+1,cy))
            visited[cx+1][cy] = True
        if 0 <= cy-1 < n and not visited[cx][cy-1] and get_block_info(area[cx][cy])[0] == '0':
            q.append((cx,cy-1)) 
            visited[cx][cy-1] = True
        if 0 <= cy+1 < n and not visited[cx][cy+1] and get_block_info(area[cx][cy])[2] == '0':
            q.append((cx,cy+1))
            visited[cx][cy+1] = True

    return count

for i in range(m):
    for j in range(n):
        result = bfs(i,j)
        
        if result != -1:
            answer.append(result)

for i in range(m):
    for j in range(n):
        block_info = get_block_info(area[i][j])

        if block_info[0] == '1':
            visited = [[False]*n for _ in range(m)]
            area[i][j] -= 1
            maximum = max(maximum,bfs(i,j))
            area[i][j] += 1

        if block_info[1] == '1':
            visited = [[False]*n for _ in range(m)]
            area[i][j] -= 2
            maximum = max(maximum,bfs(i,j))
            area[i][j] += 2 

        if block_info[2] == '1':
            visited = [[False]*n for _ in range(m)]
            area[i][j] -= 4
            maximum = max(maximum,bfs(i,j))
            area[i][j] += 4
 
        if block_info[3] == '1':
            visited = [[False]*n for _ in range(m)]
            area[i][j] -= 8
            maximum = max(maximum,bfs(i,j))
            area[i][j] += 8

print(len(answer))
print(max(answer))
print(maximum)