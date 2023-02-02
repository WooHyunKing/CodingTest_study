# n = int(input())
# data = list(map(int,input().split()))

# data.sort(reverse=True) # 동전의 금액을 내림차순으로 정렬

# result = 1 # 결과(답)은 1부터 시작

# while result <= sum(data): # 끝까지 답이 나오지 않으면 정답(최소값)은 '동전의 금액 총합 + 1'

#     number = result

#     for i in range(len(data)): # 동전의 금액 별로 반복

#         if data[i] <= number: # 동전의 금액이 현재 값보다 작거나 같은 경우
#             number -= data[i] # 일단 현재 값에서 동전의 금액만큼 뺀다

#     if number == 0: # 동전의 금액 별로 전부 빼봤을 때 현재 값이 0 인 경우(만들 수 있는 금액인 경우)
#         result += 1 # 다음 수로 넘어간다

#     else: # 동전의 금액 별로 전부 빼봐도 현재 값이 0이 아닌 경우(만들 수 없는 금액인 경우)
#         break # 그 값이 곧 정답

# print(result)

#################################################

# n = int(input())
# data = list(map(int,input().split()))

# data.sort(reverse=True)

# solution = 1

# while(solution <= sum(data)):

#     temp = solution
#     temp2 = solution

#     for i in data:
#         if((temp - i) == 0):
#             temp -= i
#             break
#         elif((temp - i) > 0 ):
#             temp -= i
#         else:
#             continue

#     if(temp > 0):
#         solution = temp2
#         break
#     solution += 1

# print(solution)

#################################################

n = int(input())
data = list(map(int,input().split()))

data.sort()

target = 1
for i in data:
    # 만들 수 없는 금액을 찾았을 경우 반복문 종료
    if target < i:
        break
    target += i

# 만들 수 없는 최소 금액 출력
print(target)
