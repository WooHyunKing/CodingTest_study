import sys
from itertools import permutations

input = sys.stdin.readline

# 레일의 순서를 조작해서 최소한의 무게만 들 수 있게 일을 함
# N개의 레일, 각 레일은 Ni 무게 전용 레일로 주어진다.(같은 무게의 레일 X)

# 레일의 순서가 정해지면 택배 바구니 무게(M)를 넘어가기 전까지 택배 바구니에 택배를 담아 들고 옮겨야 함
# 레일 순서대로 택배를 담되, 바구니 무게를 초과하지 않은 만큼 담아서 이동하게 되면 1번 일한 것으로 쳐줌
# (단, 택배는 순서대로 담아야 하므로 레일의 순서를 건너 뛸 순 없다)

# 총 k번 일을 하는데 최소한의 무게로 일을 할 수 있도록 하자

n, m, k = map(int,input().split())

weights = list(map(int,input().split()))

cases = list(permutations(weights))

answer = float("inf")

def get_work(weight_list):

    current_weight = 0
    temp_k = 0
    i = -1
    work = 0

    while True:

        if current_weight + weight_list[(i+1)%n] > m:
            temp_k += 1
            current_weight = weight_list[(i+1)%n]
            if temp_k >= k:
                break
        else:
            current_weight += weight_list[(i+1)%n]
        
        work += weight_list[(i+1)%n]

        if i == (n-1):
            i = 0
        else:
            i += 1
    return work

for case in cases:
    result = get_work(case)
    if result < answer:
        answer = result

print(answer)