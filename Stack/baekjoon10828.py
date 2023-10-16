n = int(input())

command_list = [list(input().split()) for _ in range(n)]

stack = []

def push(x):
    stack.append(x)

def pop(): 
    if stack:
        print(stack.pop())
    else:
        print(-1)

def size():
    print(len(stack))

def empty():
    if stack:
        print(0)
    else:
        print(1)

def top():
    if stack:
        print(stack[-1])
    else:
        print(-1)

for command in command_list:
    if len(command) == 2: 
        push(command[1])
    else:
        if command[0] == 'pop':
            pop()
        elif command[0] == 'size':
            size()
        elif command[0] == 'empty':
            empty()
        elif command[0] == 'top':
            top()