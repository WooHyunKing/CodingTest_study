# array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

# def quick_sort(array,start,end):
#     if start >= end: # 원소가 1개인 경우 종료
#         return
#     pivot = start # 피벗은 첫 번째 원소
#     left = start+1
#     right = end

#     while left <= right:
#         # 피벗보다 큰 데이터를 찾을 때까지 반복
#         while left <= end and array[left] <= array[pivot]:
#             left += 1

#         # 피벗보다 작은 데이터를 찾을 때까지 반복
#         while right > start and array[right] >= array[pivot]:
#             right -= 1
        
#         if left>right: # 만약에 엇갈렸다면 작은 데이터와 피벗을 교체
#             array[right], array[pivot] = array[pivot], array[right]
        
#         else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
#             array[left], array[right] = array[right], array[left]

#     print(array)

#     quick_sort(array,start,right-1)
#     quick_sort(array,right+1,end)

# quick_sort(array,0,len(array)-1)
# print(array)

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array,start,end):
    if start >= end : # 원소가 1개인 경우 종료
        return
    
    pivot = start
    left = start + 1
    right = end

    while left <= right: # 왼쪽과 오른쪽이 엇갈리면 반복문 종료

        while left <= end and array[left] <= array[pivot]: # 피벗보다 큰 데이터를 찾을 때까지 인덱스 + 1
            left += 1
        
        while right > start and array[right] >= array[pivot]: # 피벗보다 작은 데이터를 찾을 때까지 인덱스 - 1
            right -= 1

        if left > right: # 왼쪽과 오른쪽이 엇갈렸다면 작은 데이터(right)와 피벗을 교체
            array[right],array[pivot] = array[pivot],array[right]
        else: # 엇갈리지 않았다면 작은 데이터(left)와 큰 데이터(right)를 교체
            array[left],array[right] = array[right],array[left]
    # 엇갈렸다면 right가 바꾼 자리가 되므로 그 자리를 기준으로 분할하여 재귀
    quick_sort(array,start,right-1)
    quick_sort(array,right+1,end)

quick_sort(array,0,len(array)-1)
print(array)

