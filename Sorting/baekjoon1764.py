import sys
input = sys.stdin.readline

n, m = map(int,input().split())

list_n = []
list_m = []

count = 0
count_list = []

for i in range(n):
  list_n.append(input().rstrip())

for i in range(m):
  list_m.append(input().rstrip())

set_n = set(list_n)
set_m = set(list_m)

for i in set_m:
  if i in set_n:
    count += 1
    count_list.append(i)

count_list.sort()

print(count)
for i in count_list:
  print(i)