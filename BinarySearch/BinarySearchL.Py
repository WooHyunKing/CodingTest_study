# 이진 탐색 소스코드 구현(반복문)
# def binary_search(array,target,start,end):
#     while start<=end:
#         mid = (start+end)//2
        
#         # 찾은 경우 중간점 인덱스 반환
#         if array[mid] == target:
#             return mid
#         elif array[mid] > target:
#             end = mid-1
#         else :
#             start = mid+1

#     return None

def binary_search(array,target,start,end):
    while start <= end:
        mid = (start+end)//2
        
        if array[mid] == target:
            return mid

        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return None

def binary_search_2(array,tartget,start,end):
    while start <= end:
        mid = (start+end) // 2

        if array[mid] == target:
            return mid
        
        elif array[mid] > target:
            end = mid-1
        else:
            start = mid+1
    return None


# # n(원소의 개수)과 target(찾고자 하는 문자열) 입력받기
# n, target = list(map(int,input().split()))

# # 전체 원소 입력받기
# array = list(map(int,input().split()))

# # 이진 탐색 수행 결과 출력
# result = binary_search(array,target,0,n-1)

# if result == None :
#     print("원소가 존재하지 않습니다.")

# else:
#     print(result+1)

print(dir(dict([])))