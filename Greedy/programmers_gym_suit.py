# def solution(n, lost, reserve):
#     # 2 <= n <= 30
#     # 1 <= len(lost) <= n, 중복 X
#     # 1 <= len(reserve) <= n, 중복 X
    
#     # 여벌 체육복이 있는 학생만 다른 학생에게 빌려줄 수 있음
#     # 여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있음
    
#     status = [1]*(n+1)
    
#     for r in reserve:
#         status[r] += 1
        
#     for l in lost:
#         status[l] -= 1
        
#     for i in range(n+1):
#         if status[i] == 2:
#             if i-1 >= 0 and status[i-1] == 0:
#                 status[i] -= 1
#                 status[i-1] += 1
#             elif i+1 < n+1 and status[i+1] == 0:
#                 status[i] -= 1
#                 status[i+1] += 1
    
#     status = status[1:]
    
#     return sum([1 for x in status if x != 0 ])

def solution(n, lost, reserve):
    answer = 0
    
    # 학생들의 번호는 체격 순
    # 바로 앞 번호의 학생이나 바로 뒷 번호의 학생에게만 체육복을 빌려줄 수 있음
    
    # 최대한 많은 학생이 체육수업을 들어야 함
    
    # 여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다. 
    # 이때 이 학생은 체육복을 하나만 도난당했다고 가정하며, 남은 체육복이 하나이기에 다른 학생에게는 체육복을 빌려줄 수 없습니다.
    
    lost_set = set(lost)
    reserve_set = set(reserve)
    
    intersection = lost_set & reserve_set
    
    reserve_set -= intersection
    lost_set -= intersection
    
    count_list = [1]*(n+1)
    
    for l in lost_set:
        count_list[l] -= 1
    for r in reserve_set:
        count_list[r] += 1
    
    for i in range(1,n+1):
        
        if i-1 >= 1 and i-1 in lost_set and i in reserve_set:
            count_list[i-1] += 1
            count_list[i] -= 1
            lost_set.discard(i-1)
            reserve_set.discard(i)
            
        if i+1 < n+1 and i+1 in lost_set and i in reserve_set:
            count_list[i+1] += 1
            count_list[i] -= 1
            lost_set.discard(i+1)
            reserve_set.discard(i)
    
    for i in range(1,n+1):
        if count_list[i] > 0:
            answer += 1
    
    return answer