# n = int(input())
# m = int(input())

# count = 0

# graph = [[0]*(n+1) for _ in range(n+1)]
# visited = [0]*(n+1)

# for i in range(m):
#     a,b=map(int,input().split())
#     graph[a][b] = graph[b][a] = 1 # 양방향이므로 인접행렬로 구현

# def dfs(v):
#     global count
#     visited[v] = 1
#     count+=1

#     for j in range(1,n+1):
#         if graph[v][j] == 1 and visited[j]==0:
#             dfs(j)

# dfs(1)

# print(count-1)

from collections import deque

vertex_count = int(input())
edge_count = int(input())

graph = [[] for _ in range(vertex_count + 1)]

for _ in range(edge_count):
    x, y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False] * (vertex_count+1)

count = 0

def dfs(graph, v, visited):

    global count

    visited[v] = True
    
    count += 1
    
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

def bfs(graph,v,visited):
    
    global count

    visited[v] = True

    queue = deque([v])

    while queue:
        node = queue.popleft()
        count += 1
        
        for i in graph[node]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    

# dfs(graph,1,visited)
bfs(graph,1,visited)
print(count-1)