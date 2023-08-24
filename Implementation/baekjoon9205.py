from collections import deque

def calculate_distance(x1,y1,x2,y2):
    return abs(x1-x2) + abs(y1-y2)

def bfs(x,y):
    global end_x, end_y
    queue = deque([(x,y)])
    visited = set()

    while queue:
        x, y = queue.popleft()
        
        if calculate_distance(x,y,end_x,end_y) <= 1000:
            return True
        for i in range(n):
            store_x, store_y = store_list[i]
            if (store_x,store_y) not in visited:
                if calculate_distance(x,y,store_x,store_y) <= 1000:
                    visited.add((store_x,store_y))
                    queue.append((store_x,store_y))
    return False

t = int(input())

result = []

for _ in range(t):
    n = int(input())
    start_x, start_y = map(int,input().split())

    store_list = [tuple(map(int,input().split())) for _ in range(n)]

    end_x, end_y = map(int,input().split())
    
    available = bfs(start_x,start_y)

    if available:
        result.append("happy")
    else:
        result.append("sad")

for i in result:
    print(i)