import sys
input = sys.stdin.readline

INF = float("inf")

# 노드의 개수, 간선의 개수
n, m = map(int,input().split())

# 시작 노드 번호
start = int(input())

graph = [[] for _ in range(n+1)]

visited = [False]*(n+1)

# 최단 거리 테이블 초기화
distance = [INF]*(n+1)

for _ in range(m):
    a, b, c = map(int,input().split())
    graph[a].append((b,c))

# 방문하지 않은 노드 중에서, 가장 최단거리가 짧은 노드의 번호 반환
def get_smallest_node():
    min_value = INF
    index = 0

    for i in range(1,n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i

    return index
    
def dijkstra(start):
    # 시작 노드 초기화
    distance[start] = 0
    visited[start] = True

    for node, cost in graph[start]:
        distance[node] = cost
    
    # 시작 노드를 제외한 전체 N-1개의 노드에 대해 반복
    for i in range(n-1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서 방문처리
        now = get_smallest_node()
        visited[now] = True

        # 현재 노드와 연결된 다른 노드들 확인
        for node, cost in graph[now]:
            # 현재 노드를 거쳐서 다른 노드로 가는 거리가 더 짧은 경우 업데이트
            distance[node] = min(distance[node],distance[now]+cost)

dijkstra(start)

for i in range(1,n+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])