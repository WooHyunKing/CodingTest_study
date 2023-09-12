n,m = map(int,input().split())

data = sorted(list(map(int,input().split())))

is_used = [False]*10001

temp =[]

answer = []

def dfs():
    
    if len(temp) == m:
        answer.append(" ".join(map(str,temp)))
        return
    
    for v in data:
        if not is_used[v]:
            temp.append(v)
            is_used[v] = True
            dfs()
            temp.pop()
            is_used[v] = False

dfs()

for ans in answer:
    print(ans)