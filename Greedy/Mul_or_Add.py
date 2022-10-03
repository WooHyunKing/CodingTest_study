import time

number = list(map(int,input())) # 입력한 문자열을 정수 리스트로 변환

start_time = time.time()

result = 0

for i in range(len(number)-1): # 문자열의 길이 만큼 반복
    if number[i] <= 1 or number[i+1] <= 1: # 처리할 두 숫자 중 하나라도 값이 0이거나 1이라면
        result = number[i]+number[i+1] # 더하기 연산
        number[i+1]=result # 연산결과 저장
    else:
        result = number[i]*number[i+1] # 처리할 두 숫자 모두 2이상 이라면 곱하기 연산
        number[i+1]=result # 연산결과 저장

end_time = time.time()

print(end_time-start_time)

print(result)

# data = input()

# result=int(data[0])

# start_time = time.time()

# for i in range(1,len(data)):
#     num = int(data[i])
#     if result <= 1 or num <= 1:
#         result += num
#     else :
#         result *= num

# end_time = time.time()

# print(end_time-start_time)

# print(result)