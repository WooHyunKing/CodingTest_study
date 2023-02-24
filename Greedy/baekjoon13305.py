import sys
input = sys.stdin.readline

# n 입력받기
n = int(input())

# n-1개의 거리를 저장하는 리스트
distance = list(map(int,input().split()))
# 주유소의 리터당 가격을 저장하는 리스트
price = list(map(int,input().split()))

# 총 비용
total = 0

min_price = price[0]

for i in range(n-1):
    if price[i] < min_price:
        min_price = price[i]
    total += min_price * distance[i]

print(total)