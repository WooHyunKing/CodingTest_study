import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# 동환이의 출퇴근 길은 1~n까지 번호가 매겨진 단방향 그래프
# m개의 일방통행 도로가 존재

# 동환이의 집과 회사는 각각 정점 S, T로 나타냄 (출퇴근길은 S와 T 사이의 경로)

# S에서 T로 가는 출근 경로와 T에서 S로 가는 퇴근 경로에 모두 포함될 수 있는 정점의 개수

# 단, 출퇴근길에서 목적지 정점을 방문하고 나면 동환이는 더 이상 움직이지 않는다.
# 즉, 출근길 경로에 T는 마지막에 정확히 1번만 등장하며 퇴근길 경로도 마찬가지로 S는 마지막에 1번만 등장
# (대신 출근길에 S와 퇴근길에 T와 같이 출발지점은 여러번 등장해도 됨)

n, m = map(int,input().split())

graph = [[] for _ in range(n+1)]
graph_r = [[] for _ in range(n+1)]

answer = 0

for _ in range(m):
    start, end = map(int,input().split())

    graph[start].append(end)
    graph_r[end].append(start)

S, T = map(int,input().split())

# 탐색 종료 조건 : 목적지 노드 도착

def dfs(n,graph,visited):
    if visited[n]:
        return
    visited[n] = True

    for next in graph[n]:
        dfs(next,graph,visited)
    return

visited1 = [False] * (n+1)
visited1[T] = True
dfs(S,graph,visited1)

visited1_r = [False] * (n+1)
dfs(T,graph_r,visited1_r)

visited2 = [False] * (n+1)
visited2[S] = True
dfs(T,graph,visited2)

visited2_r = [False] * (n+1)
dfs(S,graph_r,visited2_r)

for i in range(1,n+1):
    if i == S or i == T:
        continue
    if visited1[i] and visited1_r[i] and visited2[i] and visited2_r[i]:
        answer += 1

print(answer)