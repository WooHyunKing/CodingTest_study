import sys
input = sys.stdin.readline

n, k = map(int,input().split())

array = sorted(list(map(int,input().split())))

print(array[n-k])