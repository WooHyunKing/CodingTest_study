import heapq
def solution(A,B):
    
    result = 0
    count = len(A)
    
    # A에 대한 최소 힙 / 최대 힙, B에 대한 최소 힙 / 최대 힙 
    min_heap_a, max_heap_a, min_heap_b, max_heap_b = [], [], [], []
    
    for a in A:
        heapq.heappush(min_heap_a,a)
        heapq.heappush(max_heap_a,-a)
    for b in B:
        heapq.heappush(min_heap_b,b)
        heapq.heappush(max_heap_b,-b)
    
    while count > 0: # 원소의 개수만큼 반복
        min_A, max_A, min_B, max_B = min_heap_a[0], -max_heap_a[0], min_heap_b[0], -max_heap_b[0]
        
        if min_A * max_B < min_B * max_A: # A의 최솟값 * B의 최댓값이 더 작은 경우
            heapq.heappop(min_heap_a)
            heapq.heappop(max_heap_b)
            result += (min_A * max_B)
        else: # B의 최솟값 * A의 최댓값이 더 작은 경우
            heapq.heappop(min_heap_b)
            heapq.heappop(max_heap_a)
            result += (min_B * max_A)
            
        count -= 1
        
    # while A and B: (시간초과 코드)
    #     min_A, max_A, min_B, max_B = min(A), max(A), min(B), max(B)
    #     if min_A * max_B < min_B * max_A:
    #         A.remove(min_A)
    #         B.remove(max_B)
    #         result += (min_A * max_B)
    #     else:
    #         A.remove(max_A)
    #         B.remove(min_B)
    #         result += (max_A * min_B)
        
    return result