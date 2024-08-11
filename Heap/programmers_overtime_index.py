import heapq

def solution(n, works):
    answer = 0
    
    # 야근 피로도는 남은 일의 작업량을 제곱하여 더한 값
    # Demi는 N시간 동안 야근 피로도를 최소화하도록 일을 함
    # Demi가 1시간 동안 작업량 1만큼을 처리할 수 있음
    
    # 퇴근까지 남은 N 시간과 각 일에 대한 작업량 works에 대해 야근 피로도를 최소화한 값을 리턴
    
    hq = []
    
    for work in works:
        heapq.heappush(hq,-work)
    
    for _ in range(n):
        
        if not hq:
            break
        
        mv = -heapq.heappop(hq)
        
        if mv > 0:
            heapq.heappush(hq,-(mv-1))
    
    for w in hq:
        answer += w**2
    
    return answer