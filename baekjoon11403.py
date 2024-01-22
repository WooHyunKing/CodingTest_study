from collections import deque
import sys

# (0,1) -> (1,3) -> (3,1)
# (1,2) -> (2,0) -> (0,1)

input = sys.stdin.readline

n = int(input().rstrip())

graph = [list(map(int,input().rstrip().split())) for _ in range(n)]

answer = [[0]*n for _ in range(n)]

def bfs(node,target):
    visited = [[False]*n for _ in range(n)]

    queue = deque([(node, 0)])

    while queue:
        
        curr_node, depth = queue.popleft()

        if curr_node == target and depth != 0:
            return True
        
        for next_node, value in enumerate(graph[curr_node]):
            if value == 1 and not visited[curr_node][next_node]:
                queue.append((next_node, depth + 1))
                visited[curr_node][next_node] = True
    
    return False
                
for i in range(n):
    for j in range(n):
        if bfs(i,j):
            answer[i][j] = 1

for i in range(n):
    print(" ".join(list(map(str,answer[i]))))