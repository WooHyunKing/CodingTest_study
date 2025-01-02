import sys

input = sys.stdin.readline

# 'X'는 땅을 나타내고, '.'는 바다를 나타낸다.

# 50년이 지나면, 인접한 세 칸 또는 네 칸에 바다가 있는 땅은 모두 잠겨버린다

# 상근이는 50년 후 지도를 그려보기로 했다.
# 섬의 개수가 오늘날보다 적어질 것이기 때문에, 지도의 크기도 작아져야 한다.

# 지도의 크기는 모든 섬을 포함하는 가장 작은 직사각형이다.

# 50년이 지난 후에도 섬은 적어도 한 개 있다. 
# 또, 지도에 없는 곳, 지도의 범위를 벗어나는 칸은 모두 바다이다.

R, C = map(int,input().split())

area = [list(input().rstrip()) for _ in range(R)]

dx, dy = [-1,1,0,0], [0,0,-1,1]

x_set, y_set = set(), set()

remove_list = []

for i in range(R):
    for j in range(C):
        if area[i][j] == 'X':
            count = 0

            for k in range(4):
                nx, ny = i + dx[k], j + dy[k]

                if 0 <= nx < R and 0 <= ny < C:
                    if  area[nx][ny] == '.':
                        count += 1
                else:
                    count += 1
            
            if count >= 3:
                remove_list.append((i,j))

for i, j in remove_list:
    area[i][j] = '.'

for i in range(R):
    for j in range(C):
        if area[i][j] == 'X':
            x_set.add(i)
            y_set.add(j)

for i in range(min(x_set), max(x_set)+1):
    for j in range(min(y_set), max(y_set)+1):
        print(area[i][j], end = '')
    print()