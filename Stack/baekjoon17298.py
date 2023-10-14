n = int(input())

elements = list(map(int,input().split()))

stack = []
answer = []

for i in range(n-1,-1,-1):
    while True:
        if len(stack) == 0:
            answer.append(-1)
            stack.append(elements[i])
            break

        if elements[i] < stack[-1]:
            answer.append(stack[-1])
            stack.append(elements[i])
            break
        else:
            stack.pop()

answer.reverse()

for i in answer:
    print(i,end=" ")