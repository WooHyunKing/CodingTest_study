n = int(input())

answer = []

string = ""

count = 0

def dfs(depth):

    global count
    global string
    
    if depth == n:
        count += 1
        answer.append(string)
        return
    
    for i in range(10):
        print(string)
        print(len(string))
        if len(string) > 0 and int(string[depth-1]) > i:
            continue
        string += str(i)
        dfs(depth+1)
        string = string[:-1]

dfs(0)

print(answer)
print(count)