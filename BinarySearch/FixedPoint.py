# 이진 탐색 소스코드 구현(재귀 함수)
def binary_search(array,start,end):
    if start > end:
        return None

    mid = (start+end)//2
    
    if array[mid] == mid:
        return mid
    
    elif binary_search(array,start,mid-1)==None:
        return binary_search(array,mid+1,end)
        

n = int(input())

numList = list(map(int,input().split()))

result = binary_search(numList,0,n-1)

if result==None:
    print(-1)
else:
    print(result)

