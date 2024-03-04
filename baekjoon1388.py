n, m = map(int,input().split())

area = [list(input()) for _ in range(n)]

visited = [[False]*m for _ in range(n)]

answer = 0

for i in range(n):
    for j in range(m):

        if visited[i][j]:
            continue

        visited[i][j] = True
        answer += 1

        if area[i][j] == '-':
            current_y = j+1
            while (current_y < m and area[i][current_y] == '-'):
                visited[i][current_y] = True
                current_y += 1

        elif area[i][j] == '|':
            current_x = i+1
            while (current_x < n and area[current_x][j] == '|'):
                visited[current_x][j] = True
                current_x += 1

print(answer)