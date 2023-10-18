import sys

input = sys.stdin.readline

string = list(input().rstrip())

m = int(input().rstrip())

command_list = [tuple(input().rstrip().split()) for _ in range(m)]

stack = []

for command in command_list:
    if len(command) == 1: # L / D / B인 경우
        if command[0] == 'L' and string: # L인 경우
            stack.append(string.pop())
        elif command[0] == 'D' and stack:
            string.append(stack.pop())
        elif command[0] == 'B' and string:
            string.pop()
    else: # P $ 인 경우
        string.append(command[1])

while stack:
    string.append(stack.pop())

print("".join(string))