import sys

input = sys.stdin.readline

# 각 계란에는 내구도와 무게가 정해져있다
# 계란으로 계란을 치게 되면 각 계란의 내구도는 '상대 계란의 무게'만큼 깎이게 된다

# 그리고 내구도가 0 이하가 되는 순간 계란은 깨지게 된다

# 일렬로 놓여있는 계란에 대해 왼쪽부터 차례로 들어서 한 번씩만 다른 계란을 쳐 최대한 많은 계란을 깨는 문제

# 1. 가장 왼쪽의 계란을 든다.

# 2. 손에 들고 있는 계란으로 깨지지 않은 다른 계란 중에서 하나를 친다.
# (단, 손에 든 계란이 깨졌거나 깨지지 않은 다른 계란이 없으면 치지 않고 넘어간다.)

# 3. 가장 최근에 든 계란의 한 칸 오른쪽 계란을 손에 들고 2번 과정을 다시 진행
# (단, 가장 최근에 든 계란이 가장 오른쪽에 위치한 계란일 경우 계란을 치는 과정을 종료)

# 일렬로 놓인 계란들의 내구도와 무게가 차례대로 주어졌을 때 최대 몇 개의 계란을 깰 수 있는지 알아맞춰보자.

n = int(input())

eggs = [list(map(int,input().split())) for _ in range(n)]

answer = float("-inf")

def dfs(index, count):
    
    global answer

    answer = max(answer,count)
    
    if index >= n:
        return
        
    if eggs[index][0] <= 0:
        dfs(index+1,count)

    else:
        for i in range(n):
            if i != index and eggs[i][0] > 0 and (count+(n-index)*2) > answer: # 백트래킹(가지치기)
                cr, cw = eggs[index][0], eggs[index][1]
                nr, nw = eggs[i][0], eggs[i][1]
                
                eggs[i][0] -= cw
                eggs[index][0] -= nw

                if eggs[i][0] <= 0 and eggs[index][0] <= 0:
                    
                    dfs(index+1,count+2)
                elif eggs[i][0] <= 0 or eggs[index][0] <= 0:
                    dfs(index+1,count+1)
                else:
                    dfs(index+1,count)

                eggs[i][0] += cw
                eggs[index][0] += nw
                    
dfs(0,0)

print(answer)