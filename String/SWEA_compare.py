t = int(input())

answer = []

for _ in range(t):
    valid = False
    str1 = input()
    str2 = input()

    str1_len,str2_len = len(str1), len(str2)

    for i in range(0,str2_len-str1_len+1):
        if str2[i:i+str1_len] == str1:
            valid = True
    
    if valid:
        answer.append(1)
    else:
        answer.append(0)

for i,value in enumerate(answer):
    print(f"#{i+1} {value}")