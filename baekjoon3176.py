import sys

input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)

for _ in range(n-1):

    a, b, c = map(int,input().split())

    graph[a].append((b,c))
    graph[b].append((a,c))

def dfs(n, end, values):

    global minimum
    global maximum

    if n == end:
        minimum = min(values)
        maximum = max(values)
        return
    
    for node, length in graph[n]:
        if not visited[node]:
            # minimum = min(minimum, length)
            # maximum = max(maximum, length)
            visited[n] = True
            dfs(node,end,values+[length])
            visited[n] = False
            
# dfs(2,4,[])

k = int(input())

answers = []

for _ in range(k):
    d, e = map(int,input().split())
    minimum, maximum = float("inf"), float("-inf")
    dfs(d,e,[])
    answers.append((minimum,maximum))

for ans in answers:
    print(ans[0],ans[1])