# 식의 계산은 우선 순위 무시하고 앞에서부터 진행
# 나눗셈은 몫만 취한다(//)
# 음수를 양수로 나눌 때는 음수를 양수로 바꾼 뒤 몫을 취한뒤 음수로 바꾼다

n = int(input())

data = list(map(int,input().split()))

# 0 : 덧셈 개수, 1 : 뺄셈 개수, 2 : 곱셈 개수, 3 : 나눗셈 개수
operator_count = list(map(int,input().split()))

max_value = float("-inf")
min_value = float("inf")

def divide(x,y):
    if x < 0 and y > 0:
        return -(abs(x)//y)
    else:
        return x // y

def dfs(index,n):
    global max_value
    global min_value
    
    if sum(operator_count) == 0: # 모든 연산자를 다 사용한 경우
        max_value = max(max_value,n)
        min_value = min(min_value,n)
        return
    
    if operator_count[0] > 0: # 덧셈
        operator_count[0] -= 1
        dfs(index+1, n+data[index+1])
        operator_count[0] += 1
    if operator_count[1] > 0: # 뺄셈
        operator_count[1] -= 1
        dfs(index+1, n-data[index+1])
        operator_count[1] += 1
    if operator_count[2] > 0: # 곱셈
        operator_count[2] -= 1
        dfs(index+1, n*data[index+1])
        operator_count[2] += 1
    if operator_count[3] > 0: # 나눗셈
        operator_count[3] -= 1
        dfs(index+1, divide(n,data[index+1]))
        operator_count[3] += 1

dfs(0,data[0])

print(max_value)
print(min_value)