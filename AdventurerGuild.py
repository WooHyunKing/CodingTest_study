n = int(input())
data = list(map(int,input().split()))

data.sort(reverse=True)

index = 0
count = 0

while index <= (n-1):
    index += data[index]
    count += 1

print(count)