import time

# 모범답안
# N, M, K를 공백으로 구분하여 입력받기
n,m,k = map(int,input().split())

# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int,input().split()))

total = 0

data.sort(reverse=True)

start_time = time.time()

count = int(m/(k+1))*k
count += m%(k+1)

total += count*data[0]
total += (m-count)*data[1]

end_time = time.time()

print("time : ",end_time-start_time)

print(total)

# 본인 풀이
# while m>0:
#     new_k = min(m,k)
#     total += (data[0] * new_k)
#     m -= new_k

#     if(m>0):
#         total += data[1]
#         m -= 1
