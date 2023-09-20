from collections import deque

t = int(input())

answer = []

for _ in range(t):
    n, m = map(int,input().split())

    cheese = list(map(int,input().split()))

    data = [(i+1,cheese[i]) for i in range(m)]

    queue = deque([])
    
    for _ in range(n):
        queue.append(data.pop(0))

    while queue:
        if len(queue) == 1:
            v = queue.popleft()
            answer.append(v[0])
            break
        
        index, remain = queue.popleft()

        if remain // 2 != 0:
            queue.append((index,remain//2))
        else:
            if len(data) >= 1:
                queue.append(data.pop(0))

for i,value in enumerate(answer):
    print(f"#{i+1} {value}")