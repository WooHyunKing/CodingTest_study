# 우선순위 X, 중첩괄호 X, 괄호 없어도 Ok
# 괄호 안에는 연산자 1개만 가능
# 괄호를 적절히 추가해서 최대값 만들기

n = int(input())
formula = list(input())

global max_value
max_value = float("-inf")

def calculate(num1,operator,num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == "*":
        return num1 * num2

def dfs(index,value):
    global max_value

    if index == n - 1:
        max_value = max(max_value,value)
        return

    if index + 2 < n:
        dfs(index+2, calculate(value, formula[index+1], int(formula[index+2])))
    if index + 4 < n:
        dfs(index+4, calculate(value, formula[index+1], calculate(int(formula[index+2]), formula[index+3], int(formula[index+4]))))

dfs(0,int(formula[0]))

print(max_value)