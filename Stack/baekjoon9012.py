t = int(input())

inputs = [list(input()) for _ in range(t)]

def check_vps(str):

    stack = []

    for element in str:
        if element == '(':
            stack.append(element)
        elif element == ')':
            if not stack: # 스택이 비어있는 경우
                return False
            else:
                stack.pop()
        
    if stack:
        return False

    return True

for input_data in inputs:
    if check_vps(input_data):
        print("YES")
    else:
        print("NO")