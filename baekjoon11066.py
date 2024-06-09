# 소설을 여러 장(chapter)으로 나누어 쓰는데, 각 장은 각각 다른 파일에 저장
# 소설의 모든 장을 쓰고 나서는 각 장이 쓰여진 파일을 합쳐서 최종적으로 소설의 완성본이 들어있는 한 개의 파일을 만든다

# 두 개의 파일을 합쳐서 하나의 임시파일을 만들고, 이 임시파일이나 원래의 파일을 계속 두 개씩 합쳐서 소설의 여러 장들이 연속이 되도록 파일을 합쳐나가고, 최종적으로는 하나의 파일로 합친다

# 두 개의 파일을 합칠 때 필요한 비용(시간 등)이 두 파일 크기의 합
# 최종적인 한 개의 파일을 완성하는데 필요한 비용의 총 합을 계산

# 소설의 각 장들이 수록되어 있는 파일의 크기가 주어졌을 때, 이 파일들을 하나의 파일로 합칠 때 필요한 최소비용을 계산하는 프로그램

import sys
input=sys.stdin.readline
t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int, input().split()))
    subtotal = [0]*(n+1)
    subtotal[0]=0
    for i in range(1, n+1): #누저합 구하기
        subtotal[i]=arr[i-1]
        subtotal[i]+=subtotal[i-1]
    dp=[ 
        [1e9]*n
        for _ in range(n)
    ]
    for i in range(n):
        dp[i][i] = 0 #길이가 1인 것의 최소 비용
    
    for i in range(2, n+1): #길이
        for j in range(n-i+1): #시작 인덱스
            for k in range(j, j+i-1): #하나한씩 돌음
                dp[j][j+i-1] = min(dp[j][j+i-1], dp[j][k]+dp[k+1][j+i-1]+subtotal[j+i]-subtotal[j]) 
    
    print(dp[0][n-1])

# answer = float("inf")

# def dfs(sizes,total):

#     global answer

#     if len(sizes) == 1:
#         answer = min(answer, total)
#         return
    
#     cases = list(combinations(sizes,2))

#     for c in cases:
#         indexs = [sizes.index(x) for x in c]
#         not_in_c = [x for i,x in enumerate(sizes) if i not in indexs ]
#         in_c = []
#         summary = 0

#         for tc in c:
#             # summary += sum(tc)
#             for ttc in tc:
#                 # summary += ttc
#                 in_c.append(ttc)
        
#         # print(not_in_c) # [[40], [60]]
#         # print(in_c, total) # [30, 50]
        
#         not_in_c.append(in_c)
#         # print(not_in_c) # [[50], [60], [30, 40]]
#         # print()

#         print(total, sum(in_c))
#         print(not_in_c)
#         print()

#         dfs(not_in_c, total + sum(in_c))

#     return cases

# for _ in range(t):
    
#     k = int(input())
#     sizes = list(map(int,input().split()))
#     sizes = [[x] for x in sizes]

#     dfs(sizes,0)

#     print(answer)


    