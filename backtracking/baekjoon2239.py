import sys

input = sys.stdin.readline

# 9×9 크기의 보드가 있을 때, 각 행과 각 열, 그리고 9개의 3×3 크기의 보드에
# 1부터 9까지의 숫자가 중복 없이 나타나도록 보드를 채우면 된다

# 하다 만 스도쿠 퍼즐이 주어졌을 때, 마저 끝내는 프로그램을 작성

# 9개의 줄에 9개의 숫자로 보드가 입력된다. 
# 아직 숫자가 채워지지 않은 칸에는 0이 주어진다.

# 9개의 줄에 9개의 숫자로 답을 출력
# 답이 여러 개 있다면 그 중 사전식으로 앞서는 것을 출력
# 즉, 81자리의 수가 제일 작은 경우를 출력한다.

area = [list(map(int,list(input().rstrip()))) for _ in range(9)]

row_sets = [set() for _ in range(9)]
col_sets = [set() for _ in range(9)]
area_sets = [set() for _ in range(9)]

zero_list = []

count = 0

for i in range(9):
    for j in range(9):
        if area[i][j] != 0:
            count += 1
            row_sets[i].add(area[i][j])
            col_sets[j].add(area[i][j])

            if 0 <= i <= 2:
                if 0 <= j <= 2:
                    area_sets[0].add(area[i][j])
                elif 3 <= j <= 5:
                    area_sets[1].add(area[i][j])
                elif 6 <= j <= 8:
                    area_sets[2].add(area[i][j])
            elif 3 <= i <= 5:
                if 0 <= j <= 2:
                    area_sets[3].add(area[i][j])
                elif 3 <= j <= 5:
                    area_sets[4].add(area[i][j])
                elif 6 <= j <= 8:
                    area_sets[5].add(area[i][j])
            elif 6 <= i <= 8:
                if 0 <= j <= 2:
                    area_sets[6].add(area[i][j])
                elif 3 <= j <= 5:
                    area_sets[7].add(area[i][j])
                elif 6 <= j <= 8:
                    area_sets[8].add(area[i][j])

        else:
            zero_list.append((i,j))


def get_area_index(i,j):
    if 0 <= i <= 2:
        if 0 <= j <= 2:
            return 0
        elif 3 <= j <= 5:
            return 1
        elif 6 <= j <= 8:
            return 2
    elif 3 <= i <= 5:
        if 0 <= j <= 2:
            return 3
        elif 3 <= j <= 5:
            return 4
        elif 6 <= j <= 8:
            return 5
    elif 6 <= i <= 8:
        if 0 <= j <= 2:
            return 6
        elif 3 <= j <= 5:
            return 7
        elif 6 <= j <= 8:
            return 8
        
def dfs(index):
    
    if index == len(zero_list):
        for i in range(9):
            for j in range(9):
                print(area[i][j], end="")
            print()
        exit()
    
    x, y = zero_list[index]

    for i in range(1,10):
        if i not in row_sets[x] and i not in col_sets[y] and i not in area_sets[get_area_index(x,y)]:
            area[x][y] = i
            row_sets[x].add(i)
            col_sets[y].add(i)
            area_sets[get_area_index(x,y)].add(i)
            dfs(index+1)
            row_sets[x].remove(i)
            col_sets[y].remove(i)
            area_sets[get_area_index(x,y)].remove(i)    
            area[x][y] = 0

dfs(0)   

        
# print(row_sets)
# print(col_sets)
# print(area_sets)
# print(81-count)

# def dfs(remain):

#     global area

#     print(remain)

#     for a in area:
#         print(a)
    
#     if remain >= 81:
#         for a in area:
#             print(a)
#         exit()
    
#     for i in range(9):
#         for j in range(9):
#             if area[i][j] == 0:
#                 flag = False
#                 for k in range(9,0,-1):
#                     if k not in row_sets[i] and k not in col_sets[j] and k not in area_sets[get_area_index(i,j)]:
#                         flag = True
#                         area[i][j] = k
#                         row_sets[i].add(k)
#                         col_sets[j].add(k)
#                         area_sets[get_area_index(i,j)].add(k)
#                         # if not dfs(remain+1):
#                         #     row_sets[i].remove(k)
#                         #     col_sets[j].remove(k)
#                         #     area_sets[get_area_index(i,j)].remove(k)                  
#                         #     area[i][j] = 0
#                         #     continue
#                         dfs(remain+1)
#                         row_sets[i].remove(k)
#                         col_sets[j].remove(k)
#                         area_sets[get_area_index(i,j)].remove(k)                  
#                         area[i][j] = 0
                            
#                         # row_sets[i].remove(k)
#                         # col_sets[j].remove(k)
#                         # area_sets[get_area_index(i,j)].remove(k)                  
#                         # area[i][j] = 0
#                 if not flag:
#                     # print(i,j,"XX")
#                     # print(row_sets)
#                     # print(col_sets)
#                     # print(area_sets)
#                     return False
#     return True

            

# # for i in range(9):
# #     for j in range(9):
# #         if area[i][j] == 0:
# #             for k in range(9,0,-1):
# #                 dfs(count)
# dfs(count)