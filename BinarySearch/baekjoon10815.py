n = int(input())
array_n = sorted(list(map(int,input().split())))

m = int(input())
array_m = list(map(int,input().split()))

def binary_search(array,target,start,end):

  while start <= end:
    mid = (start+end)//2

    if array[mid] == target:
      return 1
    elif array[mid] > target:
      end = mid - 1
    else:
      start = mid + 1

  return 0

for i in array_m:
  print(binary_search(array_n,i,0,n-1),end=" ")

# n = int(input())
# array_n = list(map(int,input().split()))

# m = int(input())
# array_m = list(map(int,input().split()))

# set_n = set(array_n)

# for i in array_m:
#   if i in set_n:
#     print(1,end=" ")
#   else:
#     print(0,end=" ")