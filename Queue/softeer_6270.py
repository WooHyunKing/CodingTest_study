import sys
from collections import deque

input = sys.stdin.readline

# 0m 부터 100m 까지 일정 구간들의 엘리베이터 속도를 검사
# 빌딩에서 운영되는 엘리베이터 구간은 N개의 구간으로 나뉘며, 해당 구간의 제한 속도가 주어짐
# 구간의 총 합은 100m
# 각 구간 별 구간의 길이와 제한속도 모두 양의 정수로 나뉘어짐

# 이 구간에서 제한 속도를 초과하면 서버에 초과한 만큼의 속도가 로그에 남음
# 현재 서버의 상태가 off 상태이므로 서버의 데이터를 받아볼 수 없음
# 임의의 구간의 길이와 속도를 정해서 시범운행할 때, 가장 제한 속도가 크게 벗어난 값

N, M = map(int,input().split())

length_and_limit = deque([list(map(int,input().split())) for _ in range(N)])
test_info_queue = deque([list(map(int,input().split())) for _ in range(M)])

answer = float("-inf")

while test_info_queue :

    len, fast = length_and_limit.popleft()
    t_len, t_fast = test_info_queue.popleft()

    if t_fast > fast:
        answer = max(t_fast-fast, answer)

    if t_len > len:
        test_info_queue.appendleft((t_len-len,t_fast))
    elif t_len < len:
        length_and_limit.appendleft((len-t_len,fast))

if answer == float("-inf"):
    print(0)
else:
    print(answer)