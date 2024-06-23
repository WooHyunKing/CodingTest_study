import sys

input = sys.stdin.readline

# 데이터의 중앙값을 사용하여 자동차의 평균적인 연비를 파악
# n대의 자동차를 새로 만들었지만 3대의 자동차만 테스트할 수 있는 상황

# n대의 자동차의 실제 연비 값이 주어졌을 때, q개의 질의에 대해 임의로 3대의 자동차를 골라 테스트하여
# 중앙값이 mi값이 나오는 서로 다른 경우의 수

# n개의 자동차 연비는 서로 다른 값 !

n, q = map(int,input().split())

values = sorted(list(map(int,input().split())))
length = len(values)

index = 1

test_dict = dict()
test_inputs = [int(input()) for _ in range(q)]

for v in values:
    test_dict[v] = index
    index += 1

for td in test_inputs:
    if td in test_dict:
        temp = test_dict[td]
        print((temp-1)*(length-temp))
    else:
        print(0)