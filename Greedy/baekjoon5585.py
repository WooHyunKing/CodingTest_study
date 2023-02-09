n = int(input())

change = 1000 - n

money_unit = [500,100,50,10,5,1]

count = 0

for i in money_unit:
  if change//i > 0:
    count += (change//i)
    change %= i

print(count)