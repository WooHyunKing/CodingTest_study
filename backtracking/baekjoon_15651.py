n,m = map(int,input().split())

temp = []
answer = []

def backtracking():
    
    if len(temp) == m: # 재귀 탈출 조건문
        answer.append(' '.join(map(str,temp)))
        return
    
    for i in range(1,n+1):
        temp.append(i)
        backtracking()
        temp.pop()

backtracking()

for ans in answer:
    print(ans)