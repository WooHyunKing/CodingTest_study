n, m = map(int,input().split())

count = 0

graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)

for _ in range(m):
  x, y = map(int,input().split())
  graph[x].append(y)
  graph[y].append(x)

def dfs(graph,v):

  if visited[v]:
    return False

  visited[v] = True

  for i in graph[v]:
    if not visited[i]:
      dfs(graph,i)

  return True

for i in range(1,n+1):
  if dfs(graph,i):
    count += 1

print(count)