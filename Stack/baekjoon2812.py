n, k = map(int,input().split())

number = list(input())

stack = []

for i in range(n): 
    while stack and number[i] > stack[-1] and k > 0: 
        # 현재 숫자가 stack에 있는 숫자보다 크면 stack.pop()
        # 가장 큰 숫자를 앞 쪽에 위치시키기 위함 !
        # k개 까지만 지워야 하므로 k > 0이상일 때만 수행
        stack.pop() 
        k -= 1
    stack.append(number[i])

# 만일 k개 미만으로 숫자를 지웠다면 뒤에 있는 숫자를 남은 k개 만큼 지우고 출력한다.
if k > 0:
    print(int("".join(stack[:-k])))
else:
    print(int("".join(stack)))
