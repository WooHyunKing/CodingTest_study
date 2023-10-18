string = list(input())

stack =[]

expression =""

for i,value in enumerate(string):

    if not (value == '(' or value == ')' or value=='[' or value == ']'):
        print(0)
        exit(0)
    
    if value == '(' or value == '[':
        stack.append(value)
        expression += '('
    else:
        if not stack:
            print(0)
            exit(0)
        if value == ')':
            if stack[-1] == '[':
                print(0)
                exit(0)
            if string[i-1] == '(':
                expression += '2)'
                if i+1 < len(string) and (string[i+1] == '(' or string[i+1] =='['):
                    expression += '+' 
            else:
                expression += ')*2'
                if i+1 < len(string) and (string[i+1] == '(' or string[i+1] =='['):
                    expression += '+' 
            stack.pop()
    
        if value == ']':
            if stack[-1] == '(':
                print(0)
                exit(0)
            if string[i-1] == '[':
                expression += '3)'
                if i+1 < len(string) and (string[i+1] == '(' or string[i+1] == '['):
                    expression += '+'
            else:
                expression += ')*3'
                if i+1 < len(string) and (string[i+1] == '(' or string[i+1] =='['):
                    expression += '+' 
            stack.pop()
if stack:
    print(0)
    exit(0)

print(eval(expression))
