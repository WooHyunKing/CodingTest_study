from collections import deque

# 전체 사람 수(n)
n = int(input())

# 촌수를 계산해야 하는 두 사람
target_a, target_b = map(int,input().split())

# 부모 자식들 간의 관계의 개수
m = int(input())

# 전체 사람의 부자 관계를 나타내는 2차원 리스트
graph = [[] for _ in range(n+1)]

# 확인 여부 확인용 리스트
visited = [False] * (n+1)

# 친척 관계를 저장하는 리스트
relation = [0]*(n+1)
relation[target_a] = 0

for _ in range(m):
  x, y = map(int,input().split())
  graph[x].append(y)
  graph[y].append(x)

def bfs(graph,v,visited):

  visited[v] = True

  queue = deque([v])

  while queue:

    popped =  queue.popleft()

    for i in graph[popped]:
      if not visited[i]:
        visited[i] = True
        queue.append(i)
        relation[i] = relation[popped]+1

bfs(graph,target_a,visited)

if relation[target_b] == 0:
  print(-1)
else:
  print(relation[target_b])