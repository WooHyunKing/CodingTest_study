n = list(input())

new_list = list(map(int,n))

new_list.sort(reverse=True)

for i in new_list:
  print(i,end="")