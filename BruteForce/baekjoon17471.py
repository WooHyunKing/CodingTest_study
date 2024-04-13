import sys
from collections import deque

def combination(arr,r):
    
    def generate(elements):
        if len(elements) == r:
            return [elements[:]]
        
        cases = []

        start = arr.index(elements[-1]) + 1 if elements else 0

        for i in range(start,len(arr)):
            elements.append(arr[i])
            cases.extend(generate(elements))
            elements.pop()

        return cases

    return generate([])

# 구역을 두 개의 선거구로 나눠야 하고, 각 구역은 두 선거구 중 하나에 포함되어야 한다.
# 선거구는 구역을 적어도 하나 포함해야 하고, 한 선거구에 포함되어 있는 구역은 모두 연결되어 있어야 한다.
input = sys.stdin.readline

n = int(input())

peoples = [0] + list(map(int,input().split()))

graph = [set() for _ in range(n+1)]

answer = float("inf")

visited_set = set()

def bfs(n,s): # 주어진 원소(n)에서 시작하여 방문한 원소들을 반환하는 함수

    queue = deque([])
    queue.append(n)

    visited_set.add(n)

    while queue:

        v = queue.popleft()
        
        for i in graph[v]:
            if i not in visited_set and i in s: # 다음 원소가 주어진 집합(s)에 존재하고, 방문하지 않았을 경우 방문처리
                queue.append(i)
                visited_set.add(i)

    return visited_set

def check(li): # 주어진 원소 집합이 각각 연결되어있는지 확인하는 함수(둘다 연결되어있으면 답 최신화)

    global answer 
    global visited_set

    remain = list(set([i for i in range(1,n+1)]) - set(li))

    if (bfs(remain[0],set(remain)) & set(remain) == set(remain)) and (bfs(li[0],set(li)) & set(li) == set(li)):

        answer = min(answer, abs(sum([peoples[i] for i in remain])-sum([peoples[i] for i in li])))
    
    visited_set = set()

for i in range(n):
    neighbors = list(map(int,input().split()))

    for j in range(1,len(neighbors)):
        graph[i+1].add(neighbors[j])

for i in range(1,n//2+1):
    cases = list(combination([i for i in range(1,n+1)], i))

    for c in cases:
        check(c)

if answer == float("inf"): # 두 선거구로 나눌 수 없는 경우
    print(-1)
else:
    print(answer)