import sys
from collections import deque

# 회전하는 벨트 위에 여러 가지 종류의 초밥이 접시에 담겨 놓여 있고, 손님은 이 중에서 자기가 좋아하는 초밥을 골라서 먹는다

# 1. 벨트의 임의의 한 위치부터 k개의 접시를 연속해서 먹을 경우 할인된 정액 가격으로 제공
# 2. 각 고객에게 초밥의 종류 하나가 쓰인 쿠폰을 발행하고, 1번 행사에 참가할 경우 이 쿠폰에 적혀진 종류의 초밥 하나를 추가로 무료로 제공
# (만약 이 번호에 적혀진 초밥이 현재 벨트 위에 없을 경우, 요리사가 새로 만들어 손님에게 제공)

input = sys.stdin.readline

n, d, k, c = map(int,input().split())

dictionary = [0]*(d+1)

sushi_list = []

for _ in range(n):
    menu = int(input())
    # dictionary[menu] += 1
    sushi_list.append(menu)

for i in range(k):
    dictionary[sushi_list[i]] += 1

sushi_list *= 2

value = deque(sushi_list[:k])
value_set = set(value)
# value_set.discard(c)
value_count = len(value_set)

answer = 0


for i in range(k,n+k):

    dictionary[sushi_list[i-k]] -= 1

    temp = value_count

    if dictionary[sushi_list[i-k]] <= 0:
        temp -= 1
    
    if dictionary[sushi_list[i]] <= 0:
        temp += 1

    dictionary[sushi_list[i]] += 1


    if dictionary[c] <= 0:
        answer = max(answer,temp+1)
    else:
        answer = max(answer,temp)

    value_count = temp


print(answer)