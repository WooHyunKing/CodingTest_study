n, m = map(int,input().split())

h = list(map(int,input().split()))

def getUnhappy(num):
    total = 0
    
    for i in range(1,num+1):
        total += i**2
    
    return total

happy = sum(h) + len(h)
unhappy = m - happy

area = [0] * (n+1)

index = 0

for i in range(unhappy):
    area[index] += 1
    index += 1

    if index >= n+1:
        index = 0

print(sum([getUnhappy(x) for x in area]))