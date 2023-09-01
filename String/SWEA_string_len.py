t = int(input())

answer = []

for _ in range(t):
    str1 = list(input())
    str2 = list(input())

    str1_set = set(str1)

    result = []

    for i in str1_set:
        result.append((i,str2.count(i)))
    
    result.sort(key=lambda x:x[1])
    
    answer.append(result[-1][1])

for i,value in enumerate(answer):
    print(f"#{i+1} {value}")