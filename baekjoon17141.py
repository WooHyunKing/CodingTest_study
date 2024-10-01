# 연구소의 특정 위치에 바이러스 M개를 놓을 것이고, 승원이의 신호와 동시에 바이러스는 퍼지게 된다.
# 연구소는 빈 칸, 벽으로 이루어져 있으며, 벽은 칸 하나를 가득 차지한다.

# 0은 빈 칸, 1은 벽, 2는 바이러스를 놓을 수 있는 칸

# 일부 빈 칸은 바이러스를 놓을 수 있는 칸이다. 바이러스는 상하좌우로 인접한 모든 빈 칸으로 동시에 복제되며, 1초가 걸린다.

# 연구소의 모든 빈 칸에 바이러스가 있게 되는 최소 시간을 출력
#  바이러스를 어떻게 놓아도 모든 빈 칸에 바이러스를 퍼뜨릴 수 없는 경우에는 -1을 출력

import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int,input().split())

area = [list(map(int,input().split())) for _ in range(N)]

start_available = []

dx, dy = [-1,1,0,0], [0,0,-1,1]

answer = []

for i in range(N):
    for j in range(N):
        if area[i][j] == 2:
            start_available.append((i,j))

# print(start_available)
# print()

def combination(coors, k):

    cases = []
    
    def dfs(elements,index):
        
        if len(elements) == k:
            cases.append(elements)
            return
        
        for i in range(index+1,len(coors)):
            dfs(elements + [coors[i]],i)

    dfs([],-1)
    
    return cases

virus_cases = combination(start_available,M)

for virus_case in virus_cases:
    # print(virus_case)

    visited = [[-1]*N for _ in range(N)]

    flag = True

    max_time = float("-inf")

    for vx, vy in virus_case:
        visited[vx][vy] = 0

    q = deque(virus_case)

    while q:
        cx, cy = q.popleft()
        
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < N and 0 <= ny < N and area[nx][ny] != 1 and visited[nx][ny] == -1:
                visited[nx][ny] = visited[cx][cy] + 1
                q.append((nx,ny))
    # for v in visited:
    #     print(v)
    # print()

    for i in range(N):
        for j in range(N):

            if area[i][j] != 1:
                max_time = max(max_time,visited[i][j])

            if area[i][j] != 1 and visited[i][j] == -1:
                flag = False
            
    
    if not flag:
        continue
    
    else:
        answer.append(max_time)

if not answer:
    print(-1)
else:
    print(min(answer))