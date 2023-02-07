# 회의실 배정

n = int(input())
list = []

count = 0
last_time = 0

for i in range(n):
    start, end = map(int,input().split())
    list.append((start,end))

# 시작시간 기준으로 오름차순 정렬
list.sort(key=lambda x:x[0])

# 종료시간 기준으로 오름차순 정렬
list.sort(key=lambda x:x[1])

# 회의 시간이 겹치지 않도록 회의 선정
for i in list:
    if i[0] >= last_time:
        count += 1
        last_time = i[1]

print(count)