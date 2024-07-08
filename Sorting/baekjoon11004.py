import sys

input = sys.stdin.readline

n,k = map(int,input().split())

numbers = sorted(list(map(int,input().split())))

print(numbers[k-1])