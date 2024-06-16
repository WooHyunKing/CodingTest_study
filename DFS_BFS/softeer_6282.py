import sys
from collections import deque

# 1 - 장애물, 0 - 도로
# 장애물 블록수 + 각 블록에 속하는 장애물의 수를 오름차순으로 정렬

input = sys.stdin.readline

dx, dy = [-1,1,0,0], [0,0,-1,1]

N = int(input())

area = [list(map(int,list(input()))) for _ in range(N)]
visited = [[False]*N for _ in range(N)]

answer = []

def bfs(x,y):
    
    queue = deque([(x,y)])
    visited[x][y] = True

    count = 1

    while queue:

        cx, cy = queue.popleft()

        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]

            if 0 <= nx < N and 0 <= ny < N and area[nx][ny] == 1 and not visited[nx][ny]:
                queue.append((nx,ny))
                visited[nx][ny] = True
                count += 1
                
    return count

for i in range(N):
    for j in range(N):
        if not visited[i][j] and area[i][j] == 1:
            answer.append(bfs(i,j))

answer.sort()

print(len(answer))

for i in answer:
    print(i)