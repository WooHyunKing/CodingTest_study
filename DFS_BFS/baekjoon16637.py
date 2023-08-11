# 우선순위 X, 중첩괄호 X, 괄호 없어도 Ok
# 괄호 안에는 연산자 1개만 가능
# 괄호를 적절히 추가해서 최대값 만들기

n = int(input())
formula = list(input())

# 최대값 초기화
max_value = float("-inf")

# 주어진 값 2개를 연산하는 함수
def calculate(num1,operator,num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == "*":
        return num1 * num2

def dfs(index,value):
    global max_value

    # dfs로 마지막 값까지 계산을 마쳤을 경우
    if index == n - 1:
        max_value = max(max_value,value)
        return
    
    # 1. 괄호로 묶지 않고 현재 숫자와 바로 다음 숫자와 연산
    if index + 2 < n:
        dfs(index+2, calculate(value, formula[index+1], int(formula[index+2])))
    # 2. 다음 숫자와 다다음 숫자를 괄호로 묶고 연산한 결과를 현재 숫자와 연산
    if index + 4 < n:
        dfs(index+4, calculate(value, formula[index+1], calculate(int(formula[index+2]), formula[index+3], int(formula[index+4]))))

# 첫 번째 값부터 시작하여 dfs 알고리즘 실행
dfs(0,int(formula[0]))

print(max_value)