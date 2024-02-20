import heapq

n = int(input())

courses = [tuple(map(int,input().split())) for _ in range(n)]

# times = [[0,0,0] for _ in range(1000000000)]

# answer = float("-inf")

# for number, start, end in courses:
#     times[start][0] += 1
#     times[end][2] += 1
#     for i in range(start+1,end):
#         times[i][1] += 1

# for front, mid, back in times:

#     if front + mid > answer:
#         answer = front + mid

# print(answer)

courses.sort(key=lambda x:x[1]) # 강의 시작 순서로 오름차순 정렬

heap = []

count = 0

for i in courses:
    while heap and heap[0] <= i[1]:
        heapq.heappop(heap)
    
    heapq.heappush(heap,i[2])

    count = max(count,len(heap))

print(count)