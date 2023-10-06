#1번 선거구 : 1 <= r < x+d1 , 1 <= c <= y
#2반 선거구 : 1 <= r <= x+d2 , y < c <= N
#3번 선거구 : x+d1 <= r <= N , 1 <= c < y-d1+d2
#4번 선거구 : x+d2 < r <= N , y-d1+d2 <= c <= N

n = int(input())

area = [list(map(int,input().split())) for _ in range(n)]

