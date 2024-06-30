import sys
from collections import deque
input = sys.stdin.readline

# 필드에 여러 가지 색깔의 뿌요를 놓는다
# 뿌요는 중력의 영향을 받아 아래에 바닥이나 다른 뿌요가 나올 때까지 아래로 떨어진다.

# 뿌요를 놓고 난 후, 같은 색 뿌요가 4개 이상 상하좌우로 연결되어 있으면 연결된 같은 색 뿌요들이 한꺼번에 없어진다
# 이때 1연쇄가 시작된다.

# 뿌요들이 없어지고 나서 위에 다른 뿌요들이 있다면, 역시 중력의 영향을 받아 차례대로 아래로 떨어지게 된다.
# 아래로 떨어지고 나서 다시 같은 색의 뿌요들이 4개 이상 모이게 되면 또 터지게 되는데, 터진 후 뿌요들이 내려오고 다시 터짐을 반복할 때마다 1연쇄씩 늘어난다.

# 터질 수 있는 뿌요가 여러 그룹이 있다면 동시에 터져야 하고 여러 그룹이 터지더라도 한번의 연쇄가 추가된다.

# 상대방의 필드가 주어졌을 때, 연쇄가 몇 번 연속으로 일어날지 계산

# '.'은 빈공간이고 '.이 아닌 것'은 각각의 색깔의 뿌요
# R은 빨강, G는 초록, B는 파랑, P는 보라, Y는 노랑

area = [list(input().rstrip()) for _ in range(12)]

dx, dy = [-1,1,0,0], [0,0,-1,1]

answer = 0

def bfs(x,y,color):

    queue = deque([(x,y)])
    boom_set = set()
    count = 0

    while queue:

        tx, ty = queue.popleft()
        
        visited[tx][ty] = True
        boom_set.add((tx,ty))
        count += 1

        for i in range(4):
            nx, ny = tx +  dx[i], ty + dy[i]

            if 0 <= nx < 12 and 0 <= ny < 6 and area[nx][ny] == color and not visited[nx][ny]:
                queue.append((nx,ny))
    
    if count >= 4:
        return list(boom_set)
    else:
        return []

def down():
    
    for j in range(6):

        flag = False
        down_puyo_list = deque([])

        for i in range(11,-1,-1):
            if area[i][j] == '.':
                if i-1 >= 0 and area[i-1][j] != '.':
                    flag = True
            else:
                down_puyo_list.appendleft(area[i][j])
        
        if flag:
            for i in range(12):
                if i < (12-len(down_puyo_list)):
                    area[i][j] = '.'
                else:
                    area[i][j] = down_puyo_list.popleft()
        
while True:

    puyo_list = []
    boom_flag = False

    visited = [[False]*6 for _ in range(12)]

    for i in range(12):
        for j in range(6):
            if area[i][j] != '.':
                puyo_list.append((i,j)) 
                  
    for px, py in puyo_list:
        result = bfs(px,py,area[px][py])
        if result:
            for rx, ry in result:
                area[rx][ry] = '.'
            boom_flag = True
    
    if not boom_flag:
        break

    answer += 1
    down()

print(answer)