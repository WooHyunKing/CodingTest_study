n = int(input())

graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
temp = []

answer = set()

for i in range(1,n+1):
    graph[int(input())].append(i)

def dfs(index):
    global answer
    
    for i in graph[index]:
        if visited[i]:
            answer |= set(temp)
            return
        visited[i] = True
        temp.append(i)
        dfs(i)
        visited[i] = False
        temp.pop()
    
for i in range(1,n+1):
    dfs(i)

answer = sorted(list(answer))
print(len(answer))

for ans in answer:
    print(ans)