import heapq

def solution(scoville, K):
    answer = 0
    
    # 모든 음식의 스코빌 지수를 K 이상으로 만들고 싶습니다
    # 스코빌 지수가 가장 낮은 두 개의 음식을 아래와 같이 특별한 방법으로 섞어 새로운 음식을 만듭니다.
    
    # 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
    
    # 모든 음식의 스코빌 지수가 K 이상이 될 때까지 반복하여 섞습니다.
    
    hq = []
    
    for data in scoville:
        heapq.heappush(hq,data)
    
    while True:

        if hq and len(hq) == 1 and hq[0] < K:
            return -1
            
        if hq and hq[0] >= K:
            break
        
        if hq:
            a = heapq.heappop(hq)
        else:
            break
            
        if hq:
            b = heapq.heappop(hq)
        else:
            break
        
        heapq.heappush(hq,a+b*2)
        
        answer += 1
    
    return answer