area = [list(map(int,input().split())) for _ in range(10)]

size_count = [0]*5

min_value = float("inf")

def check(x,y,n): # n 크기의 색종이를 붙일 수 있는 확인하는 함수

    if (x + n - 1) >= 10 or (y + n - 1) >= 10:
        return False
    
    for i in range(n+1):
        for j in range(n+1):
            if area[x+i][y+j] == 0:
                return False
    return True

def cover(x,y,n):
    for i in range(n+1):
        for j in range(n+1):
            area[x+i][y+j] = 0

def remove(x,y,n):
    for i in range(n+1):
        for j in range(n+1):
            area[x+i][y+j] = 1
        

def dfs(x,y,count):
    global min_value

    if x >= 10:
        min_value = min(min_value,count)

    elif y >= 10:
        dfs(x+1,0,count)

    elif area[x][y] == 1:
        for i in range(5):
            if size_count[i] == 5:
                continue
            if x+i >= 10 or y + i >= 10:
                continue

            if check(x,y,i):
                cover(x,y,i)
                size_count[i] += 1
                dfs(x,y+i+1,count+1)
                size_count[i] -= 1
                remove(x,y,i)
    else:
        dfs(x,y+1,count)

dfs(0,0,0)

if min_value == float("inf"):
    print(-1)
else:  
    print(min_value)