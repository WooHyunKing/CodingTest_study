import sys
import heapq
input = sys.stdin.readline

# 정수를 하나씩 외칠때마다 지금까지 말한 수 중에서 중간값을 출력
# 짝수개라면 중간에 있는 두 수 중에서 작은 수

n = int(input())

heap1 = [] # 중간값을 포함한 이전 값 최대힙
heap2 = [] # 중간값 이후의 값 최소힙

for i in range(n):
    
    num = int(input())

    if len(heap1) == len(heap2):
        heapq.heappush(heap1,-num)
    else:
        heapq.heappush(heap2,num)

    if heap2 and heap2[0] < -heap1[0]:
        lvalue = heapq.heappop(heap1)
        rvalue = heapq.heappop(heap2)
        heapq.heappush(heap1,-rvalue)
        heapq.heappush(heap2,-lvalue)
    
    print(-heap1[0])