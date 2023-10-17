# 괄호가 쌍을 이뤄서 pop될 때마다 +1
# 레이저인 경우 +현재 스택에 쌓인 개수

datas = list(input())

stack = []

answer = 0

for i,data in enumerate(datas):

    if data == '(':
        stack.append(data)
    elif data == ')':
        if datas[i-1] == '(': # 레이저인 경우
            answer += (len(stack)-1)
            stack.pop()
        else: # 막대기가 끝난 경우
            answer += 1
            stack.pop()

print(answer)