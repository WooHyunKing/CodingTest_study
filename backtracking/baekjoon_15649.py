n, m = map(int,input().split())

is_used = [False]*9

temp = []

answer = []

def backtracking():
    global is_used
    global temp
    global answer
    
    if len(temp) == m:
        answer.append(' '.join(map(str,temp)))
        return
    for i in range(1,n+1):
        if not is_used[i]:
            is_used[i] = True
            temp.append(i)
            backtracking()
            is_used[i]= False
            temp.pop()

backtracking()   

for ans in answer:
    print(ans)