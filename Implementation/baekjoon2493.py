n = int(input())

tops = list(map(int,input().split()))

answer = [0 for _ in range(n)]

stack = []

for i,value in enumerate(tops):
    while stack:
        if stack[-1][1] <= value:
            stack.pop()
        else:
            answer[i] = stack[-1][0]
            break
    if len(stack) == 0:
        answer[i] = 0
    stack.append((i+1,value))
            
print(' '.join(str(s) for s in answer))