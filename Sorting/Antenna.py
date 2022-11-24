n = int(input())
house = list(map(int,input().split()))

# 시간 초과 코드
# minimum = sum(house)
# result = 0

# for i in house:
#     summary = 0
#     for j in range(n):
#         summary += abs(house[j] - i)
    
#     if summary < minimum:
#         minimum = summary
#         result = i

# 정렬 후 중간 값이 정답
house.sort()
print(house[(n-1)//2])

