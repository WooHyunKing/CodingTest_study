def solution(s):
    answer = True
    stack = []
    
    for item in s:
        if len(stack) == 0:
            stack.append(item)
        elif stack[-1] == '(':
            if item == ')':
                stack.pop()
            elif item == '(':
                stack.append(item)
        else:
            stack.append(item)
            
    if len(stack) != 0:
        return False

    return True