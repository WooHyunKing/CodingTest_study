import time

number = list(map(int,input()))

start_time = time.time()

result = 0

for i in range(len(number)-1):
    if number[i] == 0 or number[i+1] == 0 or number[i] == 1 or number[i+1] == 1:
        result = number[i]+number[i+1]
        number[i+1]=result
    else:
        result = number[i]*number[i+1]
        number[i+1]=result

end_time = time.time()

print(end_time-start_time)

print(result)