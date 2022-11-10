n,m,v =map(int,input().split())

# 행렬 만들기
graph = [[0]*(n+1) for _ in range(n+1)]

for i in range(m):
    a,b=map(int,input().split())
    graph[a][b] = graph[b][a] = 1 # 양방향이므로 인접행렬로 구현

# 방문 리스트 행렬
visited1 = [0]*(n+1)
visited2 = visited1.copy()

# dfs 함수 만들기
def dfs(v):
    visited1[v] = 1 # 방문 처리
    print(v,end=' ')
    for i in range(1,n+1):
        if graph[v][i] == 1 and visited1[i] == 0:
            dfs(i)

# bfs 함수 만들기
def bfs(v):
    queue = [v]
    visited2[v] = 1

    while queue:
        v=queue.pop(0) # 방문 노드 제거
        print(v,end=' ')
        for i in range(1,n+1):
            if(graph[v][i] == 1 and visited2[i]==0):
                queue.append(i)
                visited2[i] = 1

dfs(v)
print()
bfs(v)
    

    