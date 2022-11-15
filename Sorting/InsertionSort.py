array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1,len(array)): # 두번째 원소(index=1)부터 시작
    for j in range(i,0,-1): # step에 -1이 들어가면 start 인덱스(i)부터 시작해서 end+1 인덱스(1)까지 1씩 감소한다.(인덱스 i부터 1까지 감소하며 반복하는 문법)
        if array[j] < array[j-1]: # 한칸씩 왼쪽으로 이동
            array[j], array[j-1] = array[j-1], array[j]

        else : # 자신보다 작은 데이터를 만나면 그 위치에서 멈춤
            break
            
print(array)