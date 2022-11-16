# 이진 탐색
n = int(input())
current = list(map(int,input().split()))
m = int(input())
require = list(map(int,input().split()))

current.sort()

def binary_search(array,target,start,end):

    while start<=end:
        mid = (start+end) // 2

        if array[mid] == target:
            return mid

        elif array[mid] > target:
            end = mid-1
        else:
            start = mid+1
    return None

for i in require:
    result = binary_search(current,i,0,n-1)
    if result == None:
        print("no", end=' ')
    else:
        print("yes", end=' ')

# 계수 정렬
# n = int(input())

# array = [0] * 1000001

# for i in input().split():
#     array[int(i)] = 1

# m = int(input())

# x = list(map(int,input().split()))

# for i in x:
#     if array[i] == 1:
#         print('yes', end=' ')
#     else:
#         print('no',end=' ')

# 집합 자료형 이용
# n = int(input())

# array = set(map(int,input().split()))

# m = int(input())

# x = list(map(int,input().split()))

# for i in x:
#     if i in array:
#         print('yes', end=' ')
#     else:
#         print('no', end=' ')