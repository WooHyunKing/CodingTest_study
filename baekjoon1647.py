import sys
from collections import deque

input = sys.stdin.readline


# 마을은 N개의 집과 그 집들을 연결하는 M개의 길로 이루어져 있다.(양방향)
# 각 길마다 길을 유지하는데 드는 유지비가 있다. 

# 임의의 두 집 사이에 경로가 항상 존재한다.

# 마을의 이장은 마을을 두 개의 분리된 마을로 분할할 계획을 가지고 있다.
# 마을을 분할할 때는 각 분리된 마을 안에 집들이 서로 연결되도록 분할해야 한다.

# 1. 분리된 두 마을 사이에 있는 길들은 필요가 없으므로 없앨 수 있다. 
# 2. 각 분리된 마을 안에서도 임의의 두 집 사이에 경로가 항상 존재하게 하면서 길을 더 없앨 수 있다.

# 마을의 이장은 위 조건을 만족하도록 길들을 모두 없애고 나머지 길의 유지비의 합을 최소로 하고 싶다.

n, m =  map(int,input().split())

graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)

for _ in range(m):
    a, b, c = map(int,input().split())

    graph[a].append((b,c))
    graph[b].append((a,c))

answer = float("inf")


def bfs(index):

    global answer

    q = deque([index])

    visited[index] = True

    costs = []

    while q:
        
        v = q.popleft()
        
        for next, cost in graph[v]:
            if not visited[next]:
                visited[next] = True
                q.append(next)
                costs.append(cost)
            if len(costs) == n-1:
                answer = min(answer, sum(costs)-max(costs))

# for i in range(1,n+1):
#     bfs(i)

bfs(7)

print(answer)
        
            

    

    

# def dfs(index, values):

#     global answer

#     if len(values) == n-1:
#         result = sum(values) - max(values)
#         if result < answer:
#             answer = result
#             # print(values)
#         return

#     for next, cost in graph[index]:
#         if not visited[next]:
#             visited[index] = True
#             dfs(next,values+[cost])
#             visited[index] = False

# for i in range(1,n+1):
#     dfs(i,[])

# print(answer-1)