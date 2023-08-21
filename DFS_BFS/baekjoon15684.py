n, m, h = map(int,input().split())

answer = 4

def check(): # i번에서 시작한 세로선이 i번에서 끝나는지 확인하는 함수
    
    for i in range(n):
        temp = i # 이동하는 세로선 위치
        for j in range(h):
            if ladder[j][temp] == 1: # 오른쪽이 1인 경우(오른쪽으로 가로선이 쳐져있는 경우)
                temp += 1
            elif temp > 0 and ladder[j][temp-1] == 1: # 왼쪽이 1인 경우(왼쪽으로 가로선이 쳐져있는 경우)                
                temp -= 1
        if temp != i:
            return False
    return True

def dfs(count,x,y):
    global answer
    
    if check(): # 현재 상태에서 각 출발점이 도착점으로 잘 도착하는지 확인
        answer = min(answer,count)
        return
    
    if count == 3 or answer <= count: # 도착점이 정상적이지 않으면
        # cnt 값이 3일 경우 그 다음 호출에서 cnt가 4가 되어 문제 조건 위반하므로 return
        # cnt 값이 ans 보다 크거나 같을 경우에는 그 다음 경우를 볼 필요가 없으므로 return
        return
    

    for i in range(x,h):
        if i == x: # 같은 세로줄 확인하면 y부터 확인. 세로줄 다르면 0부터 
            k = y
        else:
            k = 0

        for j in range(k,n-1):
            if ladder[i][j] == 0: # 0인 경우 가로줄 만들고, 연속된 가로선을 만들지 않기 위해 j + 2호출
                ladder[i][j] = 1
                dfs(count + 1, i, j + 2)
                ladder[i][j] = 0

ladder = [[0]*n for _ in range(h)]

for _ in range(m):
    a, b = map(int,input().split())
    ladder[a-1][b-1] = 1

dfs(0,0,0)

if answer <= 3:
    print(answer)
else:
    print(-1)