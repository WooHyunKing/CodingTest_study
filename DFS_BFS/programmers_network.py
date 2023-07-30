def solution(n, computers):
    answer = 0
    graph = [[] for i in range(n)]
    visited = [False]*n
    
    for i,row in enumerate(computers):
        for j,value in enumerate(row):
            if i != j and value == 1:
                graph[j].append(i)
                
    print(graph)
    
    def dfs(n):
        
        if visited[n]:
            return False
        
        visited[n] = True
        
        for i in graph[n]:
            if not visited[i]:
                dfs(i)
        
        return True
        
    for i in range(n):
        if dfs(i):
            answer += 1
    
    return answer