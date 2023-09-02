t = int(input())

answer = []

for _ in range(t):

    stack = []
    data = list(input())

    valid = True

    for value in data:
        if value == '(' or value == '{': # 여는 괄호일 경우 스택에 push
            stack.append(value)
        elif value == ')' or value == '}': # 닫는 괄호인 경우
            if len(stack) == 0:
                valid = False
                break
            if value == ')':
                if stack[-1] == '(':
                    stack.pop()
                else:
                    valid = False
                    break
            elif value == '}':
                if stack[-1] == '{':
                    stack.pop()
                else:
                    valid = False
                    break
    if len(stack) != 0:
        valid = False

    if valid:
        answer.append(1)
    else:
        answer.append(0)
        
for i,value in enumerate(answer):
    print(f"#{i+1} {value}")