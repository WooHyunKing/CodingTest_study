import sys
from collections import deque

input = sys.stdin.readline

# 헛간의 개수는 N(2 <= N <= 20,000)개이며, 1 부터 샌다
# 모든 헛간은 M(1<= M <= 50,000)개의 양방향 길로 이어져 있고, 그 양 끝을 A_i 와 B_i(1<= A_i <= N; 1 <= B_i <= N; A_i != B_i)
# 또한 어떤 헛간에서 다른 헛간으로는 언제나 도달 가능하다고 생각해도 좋다. 

# 재서기는 수혀니가 1번 헛간부터 찾을 것을 알고 있다

# 출력 : 숨어야 하는 헛간 번호(만약 거리가 같은 헛간이 여러개면 가장 작은 헛간 번호를 출력), 헛간까지의 거리, 헛간과 같은 거리를 갖는 헛간의 개수

n, m = map(int,input().split())

graph = [[] for _ in range(n+1)]

visited = [False]*(n+1)

answer = []

maximum = -1

for _ in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs():

    global maximum
    global answer

    q = deque([(1,0)])
    visited[1] = True

    while q:

        v, depth = q.popleft()

        if depth > maximum:
            answer = [v]
            maximum = depth
        elif depth == maximum:
            answer.append(v)
        
        for n in graph[v]:
            if not visited[n]:
                q.append((n,depth+1))
                visited[n] = True

bfs()

print(f"{min(answer)} {maximum} {len(answer)}")