from collections import deque

def solution(begin, target, words):
    if target not in words: # words 안에 없다면 0 반환
        return 0
    
    def canExchange(arr_a,arr_b): # 바꿀 수 있는 알파벳인지 확인
        diff = 0
        for i in range(len(arr_a)):
            if arr_a[i] != arr_b[i]:
                diff += 1
        if diff == 1:
            return True
        else:
            return False
    
    def bfs():
        queue = deque([(begin,0)])
        
        while queue:
            current, depth = queue.popleft()
            
            if current == target:
                return depth
            
            for word in words:
                if canExchange(current,word):
                    queue.append((word,depth+1))    
        return 0
    
    return bfs()