t = int(input())

answer = []

def binary_search_count(target,start,end):
    count = 0

    while start <= end:
        count += 1
        mid = int((start+end)/2)
        if mid == target:
            return count
        elif mid < target:
            start = mid
        elif mid > target:
            end = mid

    return None

for _ in range(t):
    p, a, b = map(int,input().split())

    a_count = binary_search_count(a,1,p)
    b_count = binary_search_count(b,1,p)

    if a_count < b_count:
        answer.append('A')
    elif a_count > b_count:
        answer.append('B')
    else:
        answer.append(0)

for i,value in enumerate(answer):
    print(f"#{i+1} {value}")