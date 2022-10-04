n,m = map(int,input().split())
weight = list(map(int,input().split()))

weight.sort()

count = 0

for _ in range(len(weight)):
    count += (len(weight) - weight.count(weight[0]))
    weight.pop(0)

print(count)
