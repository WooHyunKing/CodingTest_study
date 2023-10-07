# 끊어진 기타줄 개수 N
# 기타줄 브랜드 M

# 각 브랜드마다 판매중인 6개의 패키지의 가격, 낱개 가격
# 적어도 N개를 사기 위해 필요한 돈의 "최솟값"

n,m = map(int,input().split())

prices = [list(map(int,input().split())) for _ in range(m)]

min_package = min([x[0] for x in prices])
min_item = min([x[1] for x in prices])

if min_package/6 > min_item:
    print(min_item*n)
else:
    package_count = n // 6
    remain_item = n % 6

    answer = package_count * min_package + min(min_package,remain_item*min_item)

    print(answer)