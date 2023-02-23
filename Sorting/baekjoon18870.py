import sys
input = sys.stdin.readline

n = int(input())

array = list(map(int,input().split()))

set_a = set(array)

list_a = sorted(list(set_a))

dictionary = dict()

for i in range(len(list_a)):
    dictionary[list_a[i]]=i

for i in array:
    print(dictionary.get(i),end=" ")