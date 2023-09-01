import copy
t = int(input())

def check(s):
    for i in range(len(s)//2):
        if s[i] != s[-(i+1)]:
            return False
    return True

def reverse(array):
    arr_len = len(array)
    temp = [[0]*arr_len for _ in range(arr_len)]
    for i in range(arr_len):
        for j in range(arr_len):
            temp[j][i] = array[i][j]
    return temp
    
    
answer = [] 

for _ in range(t):
    n,m = map(int,input().split())
    area = [list(input()) for _ in range(n)]

    for i in range(n):
        for j in range(n-m+1):
            sliced = area[i][j:j+m]
            if check(sliced):
                answer.append(''.join(sliced))

    area = reverse(area)

    for i in range(n):
        for j in range(n-m+1):
            sliced = area[i][j:j+m]
            if check(sliced):
                answer.append(''.join(sliced))

for i,value in enumerate(answer):
    print(f"#{i+1} {value}")