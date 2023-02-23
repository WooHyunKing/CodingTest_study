import sys
input = sys.stdin.readline

n = int(input())
array_n = sorted(list(map(int,input().split())))

m = int(input())
array_m =list(map(int,input().split()))

dictionary = {}

for i in array_n:
    if i not in dictionary:
        dictionary[i] = 1
    else:
        dictionary[i] += 1

def binary_search(array,target,start,end):
    
    while start <= end:

        mid = (start + end)//2

        if array[mid] == target:
            return dictionary.get(target)
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return 0

for i in array_m:
    print(binary_search(array_n,i,0,n-1),end=" ")

# in 연산자의 시간복잡도를 줄이기 위해 집합(Set)자료형 사용
# set_n = set(array_n)

# for i in array_m:
#     if i in set_n:
#         print(dictionary[i],end=" ")
#     else:
#         print(0,end=" ")