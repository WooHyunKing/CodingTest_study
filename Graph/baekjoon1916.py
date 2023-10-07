n = int(input())
m = int(input())

INF = float("INF")

graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
distance = [INF]*(n+1)

for _ in range(m):
    start, end, cost = map(int,input().split())

    graph[start].append((end,cost))

target_start, target_dest = map(int,input().split())

def get_smallest_node():
    
    min_value = INF
    index = 0

    for i in range(1,n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i

    return index

def dijkstra(start_index):
    distance[start_index] = 0
    visited[start_index] = True

    for node,cost in graph[start_index]:
        distance[node] = min(distance[node],cost) # 하나의 노드에서 한 노드에 대한 간선이 2개 이상일 수 있으므로 항상 최소값으로 갱신
    
    for _ in range(n-1):
        current = get_smallest_node()
        visited[current]= True
        
        for node,cost in graph[current]:
            distance[node] = min(distance[node], distance[current]+cost)

dijkstra(target_start)

print(distance[target_dest])