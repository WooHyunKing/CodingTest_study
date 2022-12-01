n = int(input())
m = int(input())

count = 0

graph = [[0]*(n+1) for _ in range(n+1)]
visited = [0]*(n+1)

for i in range(m):
    a,b=map(int,input().split())
    graph[a][b] = graph[b][a] = 1 # 양방향이므로 인접행렬로 구현

def dfs(v):
    global count
    visited[v] = 1
    count+=1

    for j in range(1,n+1):
        if graph[v][j] == 1 and visited[j]==0:
            dfs(j)

dfs(1)

print(count-1)

    