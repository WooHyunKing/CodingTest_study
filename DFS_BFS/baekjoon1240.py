from collections import deque

n,m = map(int,input().split())

graph = [[] for _ in range(n+1)]

for _ in range(n-1): # n-1개의 간선을 입력받고, 양방향으로 저장
    start, end, distance = map(int,input().split())
    graph[start].append((end,distance))
    graph[end].append((start,distance))

cases = [tuple(map(int,input().split())) for _ in range(m)] # 노드간의 거리를 찾고자 하는 노드쌍

def dfs(start,end,distance,visited): # 그래프 탐색을 위한 DFS 함수

    if start == end: # 최종 노드에 도착한 경우 누적된 거리를 출력하고 종료
        print(distance)
        return

    for next_node,value in graph[start]: # 다음 노드번호와 거리
        if not visited[next_node]: # 만약에 아직 방문하지 않았다면
            visited[next_node] = True
            dfs(next_node,end,distance+value,visited) # 방문처리와 동시에 탐색
            visited[next_node] = False

def bfs(start,end,distance): # 그래프 탐색을 위한 BFS 함수

    queue = deque([(start,distance)])
    visited = [False]*(n+1)

    visited[start] = True

    while queue:
        current, summary = queue.popleft()

        if current == end:
            print(summary)
            return

        for next_node,value in graph[current]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append((next_node,summary + value))
    

for x, y in cases: # 노드간의 거리를 찾고자 하는 노드쌍을 DFS/BFS로 처리
    visited = [False]*(n+1)
    visited[x] = True
    # dfs(x,y,0,visited)
    bfs(x,y,0)