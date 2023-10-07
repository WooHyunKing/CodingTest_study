import heapq
import sys
input = sys.stdin.readline

INF = float("inf")

# 노드의 개수, 간선의 개수
n, m = map(int,input().split())

# 시작 노드 번호
start = int(input())

graph = [[] for _ in range(n+1)]

# 최단 거리 테이블 초기화
distance = [INF]*(n+1)

for _ in range(m):
    a, b, c = map(int,input().split())
    graph[a].append((b,c))

def dijkstra(start):

    distance[start] = 0

    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하고 큐에 삽입
    q = []

    heapq.heappush(q,(0,start))

    while q: # 큐에 원소가 남아있다면
        
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, current = heapq.heappop(q)
        
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[current] < dist:
            continue

        # 현재 노드와 연결된 다른 인접한 노드를 확인
        for node,cost in graph[current]:
            new_cost = dist + cost

            if new_cost < distance[node]:
                distance[node] = new_cost
                heapq.heappush(q,(new_cost,node))

dijkstra(start)

for i in range(1,n+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])