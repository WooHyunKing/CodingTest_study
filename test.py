# n = int(input())

# answer = []

# string = ""

# count = 0

# def dfs(depth):

#     global count
#     global string
    
#     if depth == n:
#         count += 1
#         answer.append(string)
#         return
    
#     for i in range(10):
#         print(string)
#         print(len(string))
#         if len(string) > 0 and int(string[depth-1]) > i:
#             continue
#         string += str(i)
#         dfs(depth+1)
#         string = string[:-1]

# dfs(0)

# print(answer)
# print(count)

# def binary_search(L, start, end, target):
#     if start > end:
#         return -1

# import sys
# import heapq

# v, e = map(int,input().split())

# INF = float("inf")

# graph = [[] for _ in range(v+1)]

# distance = [INF]*(v+1)

# start_node = int(input())

# for _ in range(e):
#     start, end, cost = map(int,input().split())
#     graph[start].append((end,cost))

# def dijkstra(start):
    
#     distance[start] = 0

#     q = []

#     heapq.heappush(q,(0,start))

#     while q:
#         dist, current = heapq.heappop(q)
        
#         if distance[current] < dist:
#             continue

#         for node, cost in graph[current]:
#             new_cost = dist + cost
            
#             if new_cost < distance[node]:
#                 distance[node] = new_cost
#                 heapq.heappush(q,(new_cost,node))

# dijkstra(start_node)

# for i in range(1,v+1):
#     if distance[i] == INF:
#         print("INF")
#     else:
#         print(distance[i])

count = 0

visited = [False]*5

area = [[0]*5 for _ in range(5)]

def test():
    global count
    count += 1

    area[0][0] = 1
    visited[0] = True

print(count)
print(visited)
for i in area:
    print(i)

print()
test()

print(count)
print(visited)
for i in area:
    print(i)