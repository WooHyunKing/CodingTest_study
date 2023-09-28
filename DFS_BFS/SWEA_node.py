from collections import deque

t = int(input())

answer = []

for _ in range(t):
    v, e = map(int,input().split())
    graph = [[] for _ in range(v+1)]
    visited = [0]*(v+1)

    for i in range(e):
        start, end = map(int,input().split())
        graph[start].append(end)
        graph[end].append(start)

    s, g = map(int,input().split())

    def bfs(s,g):
        visited[s] = 0

        queue = deque([s])

        while queue:
            v = queue.popleft()

            for node in graph[v]:
                if visited[node] == 0:
                    if node == g:
                        return visited[v]+1
                    queue.append(node)
                    visited[node] = visited[v]+1
        
        return 0
    
    answer.append(bfs(s,g))

for i,value in enumerate(answer):
    print(f"#{i+1} {value}")