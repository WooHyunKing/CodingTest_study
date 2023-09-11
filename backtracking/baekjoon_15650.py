n, m = map(int,input().split())

is_used = [False]*(n+1)

temp = []
answer = []

def back(start):
    
    if len(temp) == m:
        answer.append(' '.join(map(str,temp)))
        return
    for i in range(start,n+1):
        if i not in temp:
            temp.append(i)
            back(i+1)
            temp.pop()

back(1)

for ans in answer:
    print(ans)