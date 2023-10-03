from collections import deque

n, k = map(int,input().split())

aera = [-1]*100001
visited = [-1]*100001

def getNextLocation(n):
    return [n-1,n+1,n*2]

def bfs():
    visited[n] = 0
    queue = deque([n])

    while queue:
        v = queue.popleft()

        if v == k:
            return visited[v]
        
        for next in getNextLocation(v):
            if 0 <= next < 100001 and visited[next] == -1:
                visited[next] = visited[v] + 1
                queue.append(next)

    return -1

print(bfs())