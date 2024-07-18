from collections import deque

def solution(progresses, speeds):
    answer = []
    
    # 각 기능은 진도가 100%일 때 서비스에 반영
    # 각 기능의 개발속도는 모두 다르기 때문에 뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발될 수 있고, 이때 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포
    
    # 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 progresses
    # 각 작업의 개발 속도가 적힌 정수 배열 speeds
    
    # 배포는 하루에 한 번만 할 수 있으며, 하루의 끝에 이루어진다고 가정
    
    # 각 배포마다 몇 개의 기능이 배포되는지를 return
    
    progress_q = deque(progresses)
    speeds_q = deque(speeds)
    
    while progress_q:
        
        count = 0 
        
        for i in range(len(progress_q)):
            progress_q[i] += speeds_q[i]
        
        while progress_q and progress_q[0] >= 100:
            
            progress_q.popleft()
            speeds_q.popleft()
            count += 1
        
        if count > 0:
            answer.append(count)
    
    return answer