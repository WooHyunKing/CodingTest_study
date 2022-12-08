import bisect

n, x = map(int,input().split())

numList = list(map(int,input().split()))

print(bisect.bisect_right(numList,x)-bisect.bisect_left(numList,x))
