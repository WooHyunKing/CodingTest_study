import heapq

def solution(k, score):
    
    # 매일 1명의 가수가 노래를 부르고, 시청자들의 문자 투표수로 가수에게 점수를 부여
    # 매일 출연한 가수의 점수가 지금까지 출연 가수들의 점수 중 상위 k번째 이내이면 해당 가수의 점수를 명예의 전당이라는 목록에 올려 기념
    
    # 1. 프로그램 시작 이후 초기에 k일까지는 모든 출연 가수의 점수가 명예의 전당에 오름
    # 2. k일 다음부터는 출연 가수의 점수가 기존의 명예의 전당 목록의 k번째 순위의 가수 점수보다 더 높으면, 출연 가수의 점수가 명예의 전당에 오르게 되고 기존의 k번째 순위의 점수는 명예의 전당에서 내려오게 됩니다.
    # 3. 이 프로그램에서는 매일 "명예의 전당"의 최하위 점수를 발표
    
    answer = []
    
    hq = []
    
    for i in range(len(score)):
        
        if len(hq) < k:
            heapq.heappush(hq,score[i])
            # hq.append(score[i])
        else:
            if hq[0] < score[i]:
                heapq.heappop(hq)
                heapq.heappush(hq,score[i])
            # if min(hq) < score[i]:
            #     hq.remove(min(hq))
            #     hq.append(score[i])
        answer.append(min(hq))
    
    return answer