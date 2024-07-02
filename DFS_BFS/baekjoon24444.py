import sys

input = sys.stdin.readline

from collections import deque

# N개의 정점과 M개의 간선으로 구성된 무방향 그래프(undirected graph)가 주어진다
# 정점 번호는 1번부터 N번, 모든 간선의 가중치는 1

# 정점 R에서 시작하여 너비 우선 탐색으로 노드를 방문할 경우 노드의 방문 순서를 출력

n, m, r = map(int,input().split())

graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)

for _ in range(m):
    u, v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in graph:
    i.sort()

def bfs():
    
    queue = deque([r])

    visited[r] = 1

    count = 2

    while queue:
        
        v = queue.popleft()

        for next in graph[v]:
            if visited[next] == 0:
                queue.append(next)
                visited[next] = count
                count += 1

bfs()

for i in range(1,n+1):
    print(visited[i])