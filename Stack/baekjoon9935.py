string = list(input())

boom = input()
boom_length = len(boom)

stack = []

for i,value in enumerate(string):
    stack.append(value)
    if value == boom[-1] and len(stack) >= boom_length:
        if ''.join(stack[-boom_length:]) == boom:
            for j in range(boom_length):
                stack.pop()

if stack:
    print("".join(stack))
else:
    print("FRULA")