n = int(input())

set = set()

for i in range(n):
  set.add(input())

sort_array = sorted(set)
sort_array = sorted(sort_array,key= lambda x:len(x))


for i in sort_array:
  print(i)