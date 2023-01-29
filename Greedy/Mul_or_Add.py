# import time

# start_time = time.time()

# 교재풀이 : 5.888938903808594e-05
# data = input()
# result=int(data[0])

# start_time = time.time()

# for i in range(1,len(data)):
#     num = int(data[i])
#     if result <= 1 or num <= 1:
#         result += num
#     else :
#         result *= num
# print(result)

###################################

# 본인 풀이 : 1.9759619235992432
data = list(map(int,input()))

total = 0

for i in range(len(data)):
    if((total <= 1) or (data[i] <= 1)):
        total += data[i]
    else:
        total *= data[i]

print(total)


# end_time = time.time()

# print(end_time-start_time)