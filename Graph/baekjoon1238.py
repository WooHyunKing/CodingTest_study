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

def dijkstra(start):    

    distance = [INF]*(n+1)

    distance[start] = 0

    q = []

    heapq.heappush(q,(0,start))

    while q:
        d, current = heapq.heappop(q)
        
        if distance[current] < d:
            continue

        for node, cost in graph[current]:
            new_cost = d + cost
        
            if new_cost < distance[node]:
                distance[node] = new_cost
                heapq.heappush(q,(new_cost,node))

    return distance

go = dijkstra(x)

for i in range(1,n+1):
    back = dijkstra(i)
    total_length[i] = back[x]

for i in range(1,n+1):
    total_length[i] += go[i]

print(max(total_length[1:]))