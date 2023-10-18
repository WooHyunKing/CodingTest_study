from collections import deque

k= int(input())

for _ in range(k):
    v, e = map(int,input().split())

    graph = [[] for _ in range(v+1)]
    visited = [-1]*(v+1)

    answer = True

    for i in range(e):
        start,end = map(int,input().split())
        graph[start].append(end)
        graph[end].append(start)

    # max_node = sorted([(index,node) for index,node in enumerate(graph)],key=lambda x:len(x[1]))[-1]
    # print("max_node:",max_node)

    def bfs(index):
        global answer

        if visited[index] != -1:
            return

        visited[index] = 1

        queue = deque([index])

        while queue:
            
            current = queue.popleft()
            
            for node in graph[current]:
                if visited[node] == -1:
                    if visited[current] == 1:
                        visited[node] = 2
                    elif visited[current] == 2:
                        visited[node] = 1
                    queue.append(node)
                else:
                    if visited[current] == visited[node]:
                        answer= False
                        return
                    
    for i in range(1,v+1):
        bfs(i)

    

    # def dfs(index,depth):

    #     global answer
    #     visited[index] = True

    #     if depth >= 2:
    #         answer = False
    #         return
        
    #     for node in graph[index]:
    #         if not visited[node]:
    #             dfs(node,depth+1)

    # dfs(max_node[0],0)

    if answer:
        print("YES")
    else:
        print("NO")