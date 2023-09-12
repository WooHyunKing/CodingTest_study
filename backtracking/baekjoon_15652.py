n,m = map(int,input().split())

temp = []
answer = []

def backtracking(start):
    
    if len(temp) == m:
        answer.append(' '.join(map(str,temp)))
        return
    
    for i in range(start,n+1):
        temp.append(i)
        backtracking(i)
        temp.pop()

backtracking(1)

for ans in answer:
    print(ans)