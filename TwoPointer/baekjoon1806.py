n, s = map(int,input().split())

numbers = list(map(int,input().split()))

start, end, total  = 0, 0, 0

min_length = float("inf")

while True:
    
    if total >= s:
        min_length = min(min_length,end-start)
        total -= numbers[start]
        start += 1
    else:
        if end == n:
            break
        total += numbers[end]
        end += 1

if min_length == float("inf"):
    print(0)
else:
    print(min_length)