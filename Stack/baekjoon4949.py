answer = []

def check_balanced(string):

    stack = []

    for element in string:
        if element == '(' or element == '[':
            stack.append(element)
        elif element == ')':
            if not stack:
                return False
            else:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    return False
        elif element == ']':
            if not stack:
                return False
            else:
                if stack[-1] == '[':
                    stack.pop()
                else:
                    return False
    
    if stack:
        return False
    
    return True

while True:
    string = input()

    if string == '.':
        break

    if check_balanced(string):
        answer.append("yes")
    else:
        answer.append("no")
                
for ans in answer:
    print(ans)