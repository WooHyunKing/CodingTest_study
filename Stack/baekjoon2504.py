string = list(input())

stack =[]

expression =""

for i,value in enumerate(string):

    if not (value == '(' or value == ')' or value=='[' or value == ']'): # 괄호나 대괄호가 아닌 경우 예외처리
        print(0)
        exit(0)
    
    if value == '(' or value == '[': # 여는 괄호일 경우 스택에 넣고 표현식 열기
        stack.append(value)
        expression += '('
    else: # 닫는 괄호일 경우
        if not stack: # 닫을 괄호가 없는 경우 예외처리
            print(0)
            exit(0)
        if value == ')': # 닫는 괄호가 소괄호이고
            if stack[-1] == '[': # 스택의 마지막 원소가 일치하지 않으면 예외처리
                print(0)
                exit(0)
            if string[i-1] == '(': # ()이면 2를 반환하기 위해 곧바로 닫아줌
                expression += '2)'
                if i+1 < len(string) and (string[i+1] == '(' or string[i+1] =='['): # 다음 식이 새로운 식이라면 + 처리
                    expression += '+' 
            else: # (X)인 경우 X2 처리
                expression += ')*2'
                if i+1 < len(string) and (string[i+1] == '(' or string[i+1] =='['): # 다음 식이 새로운 식이라면 + 처리
                    expression += '+' 
            stack.pop() # 닫음과 동시에 스택 pop
    
        if value == ']': # 닫는 괄호가 대괄호이고
            if stack[-1] == '(': # 스택의 마지막 원소가 일치하지 않으면 예외처리
                print(0)
                exit(0)
            if string[i-1] == '[': # []이면 3을 반환하기 위해 곧바로 닫아줌
                expression += '3)'
                if i+1 < len(string) and (string[i+1] == '(' or string[i+1] == '['): # 다음 식이 새로운 식이라면 + 처리
                    expression += '+'
            else: # (X)인 경우 X3 처리
                expression += ')*3'
                if i+1 < len(string) and (string[i+1] == '(' or string[i+1] =='['): # 다음 식이 새로운 식이라면 + 처리
                    expression += '+' 
            stack.pop() # 닫음과 동시에 스택 pop

if stack: # 모든 과정이 끝나고도 스택이 남아있는 경우 남아있는 괄호가 있으므로 예외처리
    print(0)
    exit(0)

print(eval(expression))
