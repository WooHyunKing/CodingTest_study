from collections import deque

t = int(input())

answer = []

for i in range(t):
    n, m = map(int,input().split())
    data = list(map(int,input().split()))
    
    queue = deque(data)
    
    for j in range(m):
        queue.append(queue.popleft())
    
    answer.append(queue.popleft())


for i,value in enumerate(answer):
    print(f"#{i+1} {value}")