n, m = map(int,input().split())

area = [list(input()) for _ in range(n)] # 바닥

visited = [[False]*m for _ in range(n)] # 방문(카운팅)여부

answer = 0

for i in range(n):
    for j in range(m): # 모든 나무의 영역을 방문

        if visited[i][j]: # 이미 방문(카운팅)한 나무라면 Pass
            continue

        visited[i][j] = True # 방문(카운팅)처리
        answer += 1 # 카운트 + 1

        if area[i][j] == '-': # 가로 모양의 나무라면 옆으로 이어진 나무를 모두 방문(카운팅)처리
            current_y = j+1
            while (current_y < m and area[i][current_y] == '-'):
                visited[i][current_y] = True
                current_y += 1

        elif area[i][j] == '|': # 세로 모양의 나무라면 아래로 이어진 나무를 모두 방문(카운팅)처리
            current_x = i+1
            while (current_x < n and area[current_x][j] == '|'):
                visited[current_x][j] = True
                current_x += 1

print(answer)