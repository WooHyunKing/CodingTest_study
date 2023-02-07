n, k = map(int,input().split())

value = []
count = 0

for i in range(n):
  value.append(int(input()))

value.sort(reverse=True)

while k!=0:
  for i in value:
    if k//i > 0:
      count += k//i
      k %= i

print(count)