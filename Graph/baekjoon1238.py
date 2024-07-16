import sys
import heapq

input = sys.stdin.readline

# N개의 숫자로 구분된 각각의 마을에 한 명의 학생이 살고 있다.
# 이 마을 사이에는 총 M개의 단방향 도로들이 있고 i번째 길을 지나는데 Ti(1 ≤ Ti ≤ 100)의 시간을 소비

# N명의 학생이 X (1 ≤ X ≤ N)번 마을에 모여서 파티를 벌이기로 했다

n, m, x = map(int,input().split())

INF = float("inf")

graph = [[] for _ in range(n+1)]

total_length = [0]*(n+1)

for _ in range(m):
    start, end, t = map(int,input().split())
    graph[start].append((end,t))

def dijkstra(start): # 출발 노드를 설정

    distance = [INF]*(n+1) # 최단거리 테이블 초기화

    distance[start] = 0 # 출발 노드에서의 최단거리는 0

    q = []

    heapq.heappush(q,(0,start))

    while q:
        d, current = heapq.heappop(q) # 방문하지 않은 노드 중에서 가장 거리가 짧은 노드를 선택
        
        if distance[current] < d: # 이미 선택된 노드는 Pass
            continue

        for node, cost in graph[current]: # 선택한 노드에서 이동할 수 있는 다른 노드와 비용
            new_cost = d + cost # 새로운 거리 = 현재 노드까지의 최단거리 + 현재 노드에서 다음 노드까지의 거리
        
            if new_cost < distance[node]: # 새로운 거리가 다음 노드의 거리보다 짧을 경우
                distance[node] = new_cost # 최단거리 갱신
                heapq.heappush(q,(new_cost,node)) # 방문할 노드에 추가

    return distance # 시작 노드로부터 다른 노드까지의 최단거리가 저장된 1차원 리스트 반환

for i in range(1,n+1): # ( O(N * E * LogV) ) = 10^3 * 10^4 * log(10^3)
    go = dijkstra(i) # 1번부터 N번 마을까지 각각 다른 마을까지의 최단거리 구하기 ( O(E * LogV) )
    total_length[i] = go[x]

back = dijkstra(x) # X 마을에서부터 다른 마을까지 돌아가는 최단거리 구하기

for i in range(1,n+1):
    total_length[i] += back[i] # 왕복거리를 구해야 하므로 X 마을에서부터 돌아가는 최단거리 더해주기

print(max(total_length[1:]))