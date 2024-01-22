# n개가 중복없이 들어가있는 배열 존재

# 서로 다른 두 원소의 위치를 바꾸는 Swap 연산을 이용해서
# 원소들의 위치를 바꿔 서로 인접한 원소의 차가 k 이하가 되도록 함

# 단, Swap 연산을 최소화해야함

# 매개변수 : 배열 numbers, k(1~100)
# numbers의 길이 : 1~8, 값 : 1~100(중복X)

# 서로 인접한 원소의 차가 k 이하가 되도록 하는 최소 연산 횟수
# 존재하지 않다면 -1 반환

summary = -1

answer_set = set()

def solution(k,numbers):
    
    global summary

    permutation(numbers,0,0,k,len(numbers))

    if answer_set:
        answer = min(answer_set)
    else:
        answer = -1

    return answer

def permutation(numbers, depth, cnt, k, N):

    global answer_set
    global summary

    if depth == N: # Swap을 모두 마친 경우
        summary += 1
        flag = True

        for i in range(1,len(numbers)):
            if abs(numbers[i-1] - numbers[i]) > k:
                flag = False
                break
        
        if flag:
            answer_set.add(cnt)
        
    for i in range(depth,N):
        swap(numbers,depth,i)

        if depth != i:
            permutation(numbers,depth+1,cnt+1,k,N)
        else:
            permutation(numbers,depth+1,cnt,k,N)

        swap(numbers,depth,i)
        
def swap(numbers,depth,i):
    
    numbers[depth], numbers[i] = numbers[i], numbers[depth]

    return numbers
    
print(solution(70,[88,22,55,44,11,99,100,24]))