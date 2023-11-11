import heapq

def solution(ability,number):

    # 신입사원 2명 선발, 선발 후 같이 공부시킴
    # 모든 신입사원의 능력치는 정수로 표현
    # 2명이 같이 공부하면 서로의 능력을 흡수하여 두 신입사원의 능력치는
    # '공부하기 전 두 사람의 능력치의 합'이 됨

    # 교육 후 모든 신입사원의 능력치의 합을 최소화

    # 최솟값을 pop하는 시간복잡도를 최소화 하기위해 heapq 사용

    q = []

    for item in ability:
        heapq.heappush(q,item)

    for i in range(number):
        a = heapq.heappop(q)
        b = heapq.heappop(q)

        heapq.heappush(q,a+b)
        heapq.heappush(q,a+b)

    return sum(q)