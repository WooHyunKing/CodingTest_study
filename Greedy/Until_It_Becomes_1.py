import time, math
from tracemalloc import start
from unittest import result

n, k = map(int,input().split())

start_time = time.time()

count = 0

# while n != 1 :
#     if (n%k == 0):
#         n /= k
#         count += 1
#     else:
#         n -= 1
#         count += 1


while True:
    # (N == K로 나누어 떨어지는 수)가 될 때까지 1씩 빼기
    target = (n // k) * k
    count += (n - target)
    n = target

    # N이 K보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
    if n<k :
        break

    # K로 나누기
    count += 1
    n //= k

count += (n - 1)

end_time = time.time()

print("Time : ",end_time-start_time)

print(count)