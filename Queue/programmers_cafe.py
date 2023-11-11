# from collections import deque
# def solution(menu, order, k):
#     answer = 0
    
#     queue = deque([[0,menu[order[0]]]])
    
#     time = 1
    
#     while queue:
        
#         poped = False
#         queue[0][1] -= 1
        
#         if queue[0][1] <= 0:
#             queue.popleft()
#             poped = True
        
#         if time % k  == 0 and time//k <= len(order)-1:
#             index = time//k
#             queue.append([index,menu[order[index]]])
        
#         time += 1
        
#         answer = max(answer,len(queue))
        
#     return answer


# order 마다(k번째 마다) 체크

from collections import deque
def solution(menu, order, k):
    answer = 0
    queue = deque()
    for i in order:
        queue.append(menu[i])

        answer = max(answer,len(queue))

        time = k

        while queue:
            # queue[0]과 time을 비교(걸리는 시간과 남은 시간)
            if queue[0] < time:
                time -= queue[0]
                queue.popleft()
            elif queue[0] > time:
                queue[0] -= time
                break
            else:
                queue.popleft()
                break

    return answer