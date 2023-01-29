# data = input()

# zero_count = 0
# one_count = 0

# current = data[0]

# if(data[0]=="1"):
#     one_count+=1
# else:
#     zero_count+=1

# for i in range(1, len(data)):
#     if(data[i] != current):
#         if(data[i]=="1"):
#             one_count+=1
#         else:
#             zero_count+=1
#     current=data[i]

# print(min(zero_count,one_count))

data = list(map(int,input()))

zero_count = 0
one_count = 0

zero_first = True
one_first = True

for i in range(len(data)):
    if((data[i] == 0) and (zero_first == True) ):
        zero_count += 1
        zero_first = False
        one_first = True
    elif((data[i] == 1) and (one_first == True)):
        one_count += 1
        one_first = False
        zero_first = True

print(min(zero_count,one_count))
