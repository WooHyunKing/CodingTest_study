n = int(input())

used_1 = [False]*n
used_2 = [False]*(2*n)
used_3 = [False]*(2*n)

answer = 0

def dfs(row):

    global answer

    if row >= n:
        answer += 1
        return
    
    for i in range(n):
        if not used_1[i] and not used_2[row+i] and not used_3[row-i+n-1]:
            used_1[i] = True
            used_2[row+i] = True
            used_3[row-i+n-1] = True
            dfs(row+1)
            used_1[i] = False
            used_2[row+i] = False
            used_3[row-i+n-1] = False

dfs(0)
print(answer)