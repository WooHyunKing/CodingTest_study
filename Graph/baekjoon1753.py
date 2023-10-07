import sys
import heapq

input = sys.stdin.readline

v, e = map(int,input().split())

INF = float("inf")

graph = [[] for _ in range(v+1)]
distance = [INF]*(v+1)

start_node = int(input())

for _ in range(e):
    start, end, cost = map(int,input().split())
    graph[start].append((end,cost))

def dijkstra(start):
    
    distance[start] = 0
    
    q = []

    heapq.heappush(q,(0,start))
    
    while q:
        dist, current = heapq.heappop(q)
        
        if distance[current] < dist:
            continue
        
        for node, cost in graph[current]:
            new_cost = dist + cost

            if new_cost < distance[node]:
                distance[node] = new_cost
                heapq.heappush(q,(new_cost,node))

dijkstra(start_node)

for i in range(1,v+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])