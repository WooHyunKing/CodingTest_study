import time

# # 모범답안
# # N, M, K를 공백으로 구분하여 입력받기
# n,m,k = map(int,input().split())

# # N개의 수를 공백으로 구분하여 입력받기
# data = list(map(int,input().split()))

# total = 0

# data.sort(reverse=True)

# start_time = time.time()

# count = int(m/(k+1))*k
# count += m%(k+1)

# total += count*data[0]
# total += (m-count)*data[1]

# end_time = time.time()

# print("time : ",end_time-start_time)

# print(total)


# 본인 풀이
n, m, k = map(int,input().split());
arr = list(map(int,input().split()));

arr.sort(reverse=True);

a = m // (k+1);
b = m % (k+1);

total = ((arr[0]*k)+arr[1])*a + (b*arr[0]);
print(total);