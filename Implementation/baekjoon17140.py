r,c,k = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(3)]
answer = 0

def transpose(arr):
    return list(zip(*arr))

def calculate_row(index):
    row = arr[index]
    temp_dict = dict()
    sorted_row = []
    
    for i in row:
        if i == 0:
            continue
        if i in temp_dict:
            temp_dict[i] += 1
        else:
            temp_dict[i] = 1
    #print(temp_dict) # {1: 2, 2: 1}
    
    temp_list = [(i,temp_dict[i]) for i in temp_dict.keys()]
    #print(temp_list) # [(1, 2), (2, 1)]

    temp_list = sorted(temp_list, key=lambda x:(x[1],x[0]))
    #print(temp_list) # [(2, 1), (1, 2)]

    for i in temp_list:
        sorted_row.append(i[0])
        sorted_row.append(i[1])
    #print(sorted_row) # [2, 1, 1, 2]
    
    if len(sorted_row) > 100: # 정렬된 결과의 크기가 100이 넘어가면 나머지 버리기
        sorted_row = sorted_row[:100]

    return sorted_row

while True:

    if 0 <= r-1 < len(arr) and 0 <= c-1 < len(arr[0]):
        if arr[r-1][c-1] == k: # A[r][c]에 들어있는 값이 k가 되면 반복문을 멈추고 최소 시간을 출력
            break
    
    if answer > 100: # 100초가 지나도 A[r][c] = k가 되지 않으면 -1을 출력
        answer = -1
        break

    answer += 1

    temp = []

    if len(arr) >= len(arr[0]): # 행의 개수 ≥ 열의 개수인 경우
        for i,value in enumerate(arr):
            temp.append(calculate_row(i))
        max_length = max([len(item) for item in temp]) # 가장 큰 행/열 크기

        for i in range(len(temp)): # 가장 큰 행/열 크기에 맞춰 0으로 채우기
            if len(temp[i]) < max_length:
                temp[i] += ([0]*(max_length-len(temp[i])))

        if len(temp) > 100: # 행 또는 열의 크기가 100을 넘어가는 경우 나머지 버리기
            temp = temp[:100]
        arr = temp
    else: # 행의 개수 < 열의 개수인 경우
        arr = transpose(arr) # 열을 행으로 처리하기 위해 잠시 전치 처리
        for i,value in enumerate(arr):
            temp.append(calculate_row(i))

        max_length = max([len(item) for item in temp]) # 가장 큰 행/열 크기

        for i in range(len(temp)): # 가장 큰 행/열 크기에 맞춰 0으로 채우기
            if len(temp[i]) < max_length:
                temp[i] += ([0]*(max_length-len(temp[i])))

        if len(temp) > 100: # 행 또는 열의 크기가 100을 넘어가는 경우 나머지 버리기
            temp = temp[:100]
        arr = transpose(temp) # 모든 처리를 해준 후 다시 전치 처리

print(answer)