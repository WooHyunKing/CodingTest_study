from collections import deque

def solution(n, edge):
    answer = 0
    
    graph = [[] for _ in range(n+1)]
    visited = [False]*(n+1)
    route = []
    
    for start,end in edge:
        graph[start].append(end)
        graph[end].append(start)
    
    def bfs(index):
        
        visited[index] = True
        
        queue = deque([(index,0)])
        
        route.append((index,0))
        
        while queue:
            v, depth = queue.popleft()
        
            for node in graph[v]:
                if not visited[node]:
                    visited[node] = True
                    queue.append((node,depth+1))
                    route.append((node,depth+1))
        
    bfs(1)
    
    max_distance = max([x[1] for x in route])
    
    route = [x for x in route if x[1] == max_distance]
    
    return len(route)