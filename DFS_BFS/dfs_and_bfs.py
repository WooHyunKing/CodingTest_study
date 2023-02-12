# n,m,v =map(int,input().split())

# # 행렬 만들기
# graph = [[0]*(n+1) for _ in range(n+1)]

# for i in range(m):
#     a,b=map(int,input().split())
#     graph[a][b] = graph[b][a] = 1 # 양방향이므로 인접행렬로 구현

# # 방문 리스트 행렬
# visited1 = [0]*(n+1)
# visited2 = visited1.copy()

# # dfs 함수 만들기
# def dfs(v):
#     visited1[v] = 1 # 방문 처리
#     print(v,end=' ')
#     for i in range(1,n+1):
#         if graph[v][i] == 1 and visited1[i] == 0:
#             dfs(i)

# # bfs 함수 만들기
# def bfs(v):
#     queue = [v]
#     visited2[v] = 1

#     while queue:
#         v=queue.pop(0) # 방문 노드 제거
#         print(v,end=' ')
#         for i in range(1,n+1):
#             if(graph[v][i] == 1 and visited2[i]==0):
#                 queue.append(i)
#                 visited2[i] = 1

# dfs(v)
# print()
# bfs(v)

from collections import deque

n, m ,v = map(int,input().split())

graph = [[] for _ in range(n+1)]

visited_dfs = [False] * (n+1)
visited_bfs = [False] * (n+1)

# 노드와 간선 정보 받기
for _ in range(m):
    x, y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in graph:
    i.sort()

# DFS 함수 구현
def dfs(graph,start,visited):
    
    visited[start] = True

    print(start, end=" ")

    for i in graph[start]:
        if not visited[i]:
            dfs(graph,i,visited)

# BFS 함수 구현
def bfs(graph,start,visited):

    visited[start] = True

    queue = deque([start])
    
    while queue:
        node = queue.popleft()

        print(node, end=" ")

        for i in graph[node]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    
dfs(graph,v,visited_dfs)
print()
bfs(graph,v,visited_bfs)
