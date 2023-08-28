n = int(input())

area = [list(map(int,input().split())) for _ in range(n)]

inital_pipe = [(0,0),(0,1)]

answer = 0

def check_direction(status): # 가로인지 세로인지 대각선인지 파악하는 함수
    if abs(status[0][0] - status[1][0]) == 1 and abs(status[0][1] - status[1][1]) == 1:
        return "diagonal"
    elif abs(status[0][0] - status[1][0]) == 1:
        return "vertical"
    elif abs(status[0][1] - status[1][1]) == 1:
        return "horizontal"
    
def dfs(pipe):

    global answer

    if pipe[1][0] == n-1 and pipe[1][1] == n-1:
        answer += 1
        return
    
    if check_direction(pipe) == "horizontal": # 가로인 경우
        temp = pipe.pop(0)
        x, y = pipe[0][0], pipe[0][1]

        if 0 <= y+1 < n and area[x][y+1] == 0:
            pipe.append((x,y+1))
            dfs(pipe)
            pipe.pop()
        
        if 0 <= x+1 < n and 0 <= y+1 < n and area[x][y+1] == 0 and area[x+1][y] == 0 and area[x+1][y+1] == 0:
            pipe.append((x+1,y+1))
            dfs(pipe)
            pipe.pop()
        
        pipe.insert(0,temp)
        return
    
    elif check_direction(pipe) == "vertical": # 세로인 경우
        temp = pipe.pop(0)
        x, y = pipe[0][0], pipe[0][1]
        if 0 <= x+1 < n and area[x+1][y] == 0:
            pipe.append((x+1,y))
            dfs(pipe)
            pipe.pop()
        
        if 0 <= x+1 < n and 0 <= y+1 < n and area[x][y+1] == 0 and area[x+1][y] == 0 and area[x+1][y+1] == 0:
            pipe.append((x+1,y+1))
            dfs(pipe)
            pipe.pop()
        pipe.insert(0,temp)
        return
    
    elif check_direction(pipe) == "diagonal":
        temp = pipe.pop(0)
        x, y = pipe[0][0], pipe[0][1]
        if 0 <= x+1 < n and area[x+1][y] == 0:
            pipe.append((x+1,y))
            dfs(pipe)
            pipe.pop()

        if 0 <= y+1 < n and area[x][y+1] == 0:
            pipe.append((x,y+1))
            dfs(pipe)
            pipe.pop()
        
        if 0 <= x+1 < n and 0 <= y+1 < n and area[x][y+1] == 0 and area[x+1][y] == 0 and area[x+1][y+1] == 0:
            pipe.append((x+1,y+1))
            dfs(pipe)
            pipe.pop()
        pipe.insert(0,temp)
        return

if area[n-1][n-1] == 0:        
    dfs(inital_pipe)

print(answer)