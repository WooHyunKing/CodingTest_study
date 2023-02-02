import time

# n,m = map(int,input().split())
# weight = list(map(int,input().split()))

# weight.sort()

# count = 0

# for _ in range(len(weight)):
#     count += (len(weight) - weight.count(weight[0]))
#     weight.pop(0)

# print(count)

######################################################

n, m = map(int,input().split())
weight = list(map(int,input().split()))

start_time = time.time()

weight.sort()

count = 0

# 리스트 집합화(원소의 값만 추출하기 위함)
weight_set = set(weight) 
weight_value = list(weight_set)

for i in weight_value:
    tempList = [j for j in weight if j > i] # 현재 i 값보다 큰 무게를 가진 공들만 추출(리스트 컴프리헨션 사용)
    count += (weight.count(i) * len(tempList)) # (현재 i 개수) * (무게가 더 큰 공 개수) = 조합의 개수

print(count)

end_time = time.time()

print(end_time-start_time)

# 소요시간 : 0.00011277198791503906

################################################

# n, m = map(int, input().split())
# data = list(map(int, input().split()))

# start_time = time.time()

# # 1부터 10까지의 무게를 담을 수 있는 리스트
# array = [0] * 11
# for x in data:
# 	# 각 무게에 해당하는 볼링공의 개수 카운트
#     array[x] += 1
# result = 0
# # 1부터 m까지의 각 무게에 대하여 처리
# for i in range(1, m+1):
#     n -= array[i] # 무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수) 제외
#     result += array[i] * n # B가 선택하는 경우의 수와 곱하기

# print(result)

# end_time = time.time()

# print(end_time-start_time)
# 소요 시간 : 6.389617919921875e-05