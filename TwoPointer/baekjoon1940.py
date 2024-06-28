import sys

input = sys.stdin.readline
# 갑옷을 만드는 재료들은 각각 고유한 번호를 가지고 있다
# 갑옷은 두 개의 재료로 만드는데 두 재료의 고유한 번호를 합쳐서 
# M(1 ≤ M ≤ 10,000,000)이 되면 갑옷이 만들어 지게 된다

# 야철대장은 자신이 만들고 있는 재료를 가지고 갑옷을 몇 개나 만들 수 있는지 궁금해졌다

# N(1 ≤ N ≤ 15,000)개의 재료와 M이 주어졌을 때 몇 개의 갑옷을 만들 수 있는지를 구하는 프로그램

n = int(input())

m = int(input())

values = sorted(list(map(int,input().split())))

count = 0

start, end = 0, n-1

while start < end:

    summary = values[start] + values[end] 
    
    if summary < m:
        start += 1
    elif summary > m:
        end -= 1
    else:
        count += 1
        start += 1

print(count)