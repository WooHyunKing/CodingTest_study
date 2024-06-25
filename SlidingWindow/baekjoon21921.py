import sys

# X일 동안 가장 많이 들어온 방문자 수와 기간

# 1. 첫째 줄에 X일 동안 가장 많이 들어온 방문자 수를 출력
# 만약 최대 방문자 수가 0명이라면 SAD를 출력

# 2. 만약 최대 방문자 수가 0명이 아닌 경우 둘째 줄에 기간이 몇 개 있는지 출력

n, x = map(int,input().split())

input = sys.stdin.readline

visit_counts = list(map(int,input().split()))

# 1. 시간복잡도 O(N^2) 풀이
# answer = 0

# count = 0

# for i, value in enumerate(visit_counts):
#     if 0 <= i+x-1 < n:
#         summary = sum(visit_counts[i:i+x])
#         if answer == summary:
#             count += 1
#         else:
#             answer = max(answer,summary)
#             count = 1

# if answer != 0:
#     print(answer)
#     print(count)
# else:
#     print("SAD")

# 2. 시간복잡도 O(N) 풀이 - 슬라이딩 윈도우

if max(visit_counts) == 0:
    print("SAD")
    exit(0)

value = sum(visit_counts[:x])

max_value = value
max_count = 1

for i in range(x,n):
    value += visit_counts[i]
    value -= visit_counts[i-x]

    if value > max_value:
        max_value = value
        max_count = 1
    elif value == max_value:
        max_count += 1

print(max_value)
print(max_count)