import sys
from collections import deque

input = sys.stdin.readline

# 회원 사이에 서로 모르는 사람도 있지만, 몇 사람을 통하면 모두가 서로 알 수 있다
# 각 회원은 다른 회원들과 가까운 정도에 따라 점수를 받게 된다.

# 어느 회원이 다른 모든 회원과 친구이면, 이 회원의 점수는 1점
# 어느 회원의 점수가 2점이면, 다른 모든 회원이 친구이거나 친구의 친구
# 어느 회원의 점수가 3점이면, 다른 모든 회원이 친구이거나, 친구의 친구이거나, 친구의 친구의 친구

# 각 회원의 점수를 정할 때 주의할 점은 어떤 두 회원이 친구사이이면서 동시에 친구의 친구사이이면, 이 두사람은 친구사이

# 회장의 점수와 회장이 될 수 있는 모든 사람을 찾는 프로그램

n = int(input())

graph = [[] for _ in range(n+1)]

minimum = float("inf")

lists = []

while True:
    a, b = map(int,input().split())

    if a == -1 and b == -1:
        break

    graph[a].append(b)
    graph[b].append(a)

def bfs(index):

    visited = [False]*(n+1)
    visited[0] = True
    
    q = deque([(index,0)])

    score = 0

    visited[index] = True

    while q:

        v, depth = q.popleft()

        score = depth
        
        for next in graph[v]:
            
            if not visited[next]:
                visited[next] = True
                q.append((next,depth+1))

    if all(visited):
        return score
    else:
        return -1
    
for i in range(1,n+1):
    result = bfs(i)

    if result != -1:
        if result < minimum:
            minimum = result
            lists = []
            lists.append(i)
            
        elif result == minimum:
            lists.append(i)
    
print(f"{minimum} {len(lists)}")

for i in lists:
    print(i,end=" ")