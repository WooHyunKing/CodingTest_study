import time
from tracemalloc import start

n, m = map(int,input().split())

start_time = time.time()

result = 0

for i in range(n):
    data = list(map(int,input().split()))
    temp = min(data)
    if temp>result:
        result=temp

end_time = time.time()

print("time : ",end_time-start_time)

print(result)