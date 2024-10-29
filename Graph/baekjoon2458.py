import sys

input = sys.stdin.readline

N, M = map(int,input().split())

graph = [[] for _ in range(N+1)]
r_graph = [[] for _ in range(N+1)]

up_count = [0]*(N+1)
down_count = [0]*(N+1)

up_set = [set() for _ in range(N+1)]
down_set = [set() for _ in range(N+1)]

answer = 0

for _ in range(M):
    a, b = map(int,input().split())

    graph[a].append(b)
    r_graph[b].append(a)

def dfs(n,start):

    for index in graph[n]:
        if index not in up_set[start]:
            up_set[start].add(index)
            up_count[start] += 1
            dfs(index,start)

def dfs_r(n,start):

    for index in r_graph[n]:
        if index not in down_set[start]:
            down_set[start].add(index)
            down_count[start] += 1
            dfs_r(index,start)

for i in range(1,N+1):
    dfs(i,i)
    dfs_r(i,i)

for i in range(1,N+1):
    if up_count[i] + down_count[i] == N-1:
        answer += 1

print(answer)