def solution(s):
    
    stack = []
    
    for v in s:
        if v == '(':
            stack.append('(')
        elif v ==')':
            if stack:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            else:
                return False
    if stack:
        return False

    return True