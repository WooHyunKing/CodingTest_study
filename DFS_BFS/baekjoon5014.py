# 스타트링크는 총 F층으로 이루어진 고층 건물에 사무실이 있다
# 스타트링크가 있는 곳의 위치는 G층이다

# 강호가 지금 있는 곳은 S층

# 엘리베이터는 버튼이 2개밖에 없다
# U버튼은 위로 U층을 가는 버튼, D버튼은 아래로 D층을 가는 버튼
# (만약 U층 위, 또는 D층 아래에 해당하는 층이 없을 때는, 엘리베이터는 움직이지 않는다)

# 강호가 G층에 도착하려면, 버튼을 적어도 몇 번 눌러야 하는지 구하는 프로그램

# 만약, 엘리베이터를 이용해서 G층에 갈 수 없다면, "use the stairs"를 출력

from collections import deque

F, S, G, U, D = map(int,input().split())

visited = [False]*1000001

answer = float("inf")

def bfs():

    global answer
    
    visited[S] = True

    queue = deque([(S,0)])
    
    while queue:
        n,count = queue.popleft()

        if n == G:
            answer = min(answer, count)
            continue

        if n + U <= F and not visited[n + U]:
            visited[n+U] = True
            queue.append((n+U,count+1))
        
        if n - D >= 1 and not visited[n - D]:
            visited[n - D] = True
            queue.append((n - D,count+1))

bfs()

if answer == float("inf"):
    print("use the stairs")
else:
    print(answer)