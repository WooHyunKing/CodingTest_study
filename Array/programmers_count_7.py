def solution(array):
    answer = 0
    for a in array:
        for b in str(a):
            if b == '7':
                answer += 1
    return answer