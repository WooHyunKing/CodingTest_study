import sys

input = sys.stdin.readline

t = int(input().rstrip())

for _ in range(t):
    n = int(input().rstrip())
    cases = []
    flag = True

    for _ in range(n):
        cases.append(input().rstrip())

    cases.sort()

    # for i in range(len(cases)):
    #     if flag:
    #         break
    #     for j in range(i+1,len(cases)):
    #         if cases[i] in cases[j]:
    #             flag = True
    #             break

    for i in range(len(cases)-1):
        if cases[i] == cases[i+1][:len(cases[i])]:
            flag = False
            break
    
    if flag:
        print("YES")
    else:
        print("NO")