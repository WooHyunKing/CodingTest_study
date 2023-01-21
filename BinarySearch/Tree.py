# 이진 탐색 소스코드 구현(반복문)
def binary_search(array,n,m,start,end):

    while start<=end :
        average = sum(array)/n

        mid = (start+end)//2

        averageList = [average]*n

        treeResult = sum([i - j for i, j in zip(array, averageList)])
        
        # 찾은 경우 중간점 인덱스 반환
        if treeResult == m:
            return 
        elif array[mid] > target:
            end = mid-1
        else :
            start = mid+1

    return None

n, m = map(int,input().split())

treeHeight = list(map(int,input().split()))

# a = [1 , 2, 3 ,4, 5]

# b = [1]*5

# print([i - j for i, j in zip(a, b)])

