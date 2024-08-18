def solution(array):
    answer = []
    
    array = sorted([[x,i] for i,x in enumerate(array)])
    
    return array[-1]