t = int(input())

answer = []

def dfs(s,g,graph,visited):
    if s == g:
        return True

    visited[s] = True

    for v in graph[s]:
        if not visited[v]:
            if dfs(v,g,graph,visited):
                return True
    
    return False


for _ in range(t):
    
    v,e = map(int,input().split())

    graph = [[] for _ in range(v+1)]
    visited = [False for _ in range(v+1)]
    
    for _ in range(e):
        start, end = map(int,input().split())
        graph[start].append(end)
    
    s, g = map(int,input().split())
    
    if dfs(s,g,graph,visited):
        answer.append(1)
    else:
        answer.append(0)

for i,value in enumerate(answer):
    print(f"#{i+1} {value}")