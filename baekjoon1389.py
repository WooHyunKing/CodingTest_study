# 지구에 있는 모든 사람들은 최대 6단계 이내에서 서로 아는 사람으로 연결
# 임의의 두 사람이 최소 몇 단계 만에 이어질 수 있는지 계산하는 게임

# 케빈 베이컨은 미국 헐리우드 영화배우들 끼리 케빈 베이컨 게임을 했을때 나오는 단계의 총 합이 가장 적은 사람

# 유저 중에서 케빈 베이컨의 수가 가장 작은 사람
# 즉, 모든 사람과 케빈 베이컨 게임을 했을 때, 나오는 단계의 합
import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int,input().split())

graph = [set() for _ in range(n+1)]
minimum = float("inf")

for _ in range(m):
    a, b = map(int,input().split())
    graph[a].add(b)
    graph[b].add(a)

def bfs(index):

    queue = deque([index])
    visited = [False]*(n+1)
    visited[index] = True

    dis = [0]*(n+1)

    while queue:
        
        node = queue.popleft()
        
        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                dis[next_node] = dis[node]+1
                queue.append(next_node)

    return sum(dis)

for i in range(1,n+1):
    
    result = bfs(i)
    
    if result < minimum:
        minimum = result
        answer = i

print(answer)