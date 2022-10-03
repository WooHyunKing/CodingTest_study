data = input()

zero_count = 0
one_count = 0

current = data[0]

if(data[0]=="1"):
    one_count+=1
else:
    zero_count+=1

for i in range(1, len(data)):
    if(data[i] != current):
        if(data[i]=="1"):
            one_count+=1
        else:
            zero_count+=1
    current=data[i]

print(min(zero_count,one_count))
