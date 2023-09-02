t = int(input())

answer = []

for _ in range(t):
    stack = []
    string = input()

    for c in string:
        if len(stack) == 0:
            stack.append(c)
        else:
            if stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)
    answer.append(len(stack))

for i,value in enumerate(answer):
    print(f"#{i+1} {value}")