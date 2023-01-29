# n = int(input())
# data = list(map(int,input().split()))

# data.sort()

# number = 0 # 현재 그룹에 포함된 모험가의 수
# count = 0  # 총 그룹 수

# for i in range(n-1): # 공포도가 낮은 모험가부터 하나씩 확인

#     number+=1 # 현재 그룹에 해당 모험가를 포함

#     if(number)>=data[i]: # 현재 그룹에 포함된 모험가의 수가 현재 모험가의 공포도 이상이라면 그룹 결성
#         count+=1 # 총 그룹 수 증가
#         number=0 # 현재 그룹에 포함된 모험가수 초기화

# print(count) # 총 그룹 수 출력

n = int(input())

data = list(map(int,input().split()))
data.sort()

count = 0
total = 0

for i in range(n):
    count += 1
    if(count >= data[i]):
        total += 1
        count = 0

print(total)