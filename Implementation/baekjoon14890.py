n, l = map(int,input().split())

area = [list(map(int,input().split())) for _ in range(n)]


total = 0

def checkLine(line):
    inclined = [False for _ in range(n)]
    
    for i in range(n-1):
        if line[i] == line[i+1]: # 높이가 같은 경우에는 Pass
            continue
        
        if abs(line[i]-line[i+1]) >= 2: # 낮은 칸과 높은 칸의 높이 차이가 1이 아닌 경우(조건 2)
            return False
        
        if line[i] > line[i+1]: # 내리막길인 경우
            target = line[i+1] # 낮은 지점의 칸 높이
            for j in range(1,l+1): # 경사로 길이만큼 확인
                if 0 <= i+j < n:
                    if line[i+j] != target: # 낮은 지점의 칸의 높이가 모두 같지 않거나, L개가 연속되지 않은 경우(조건 3)
                        return False
                    if inclined[i+j]: # 경사로를 놓은 곳에 또 경사로를 놓는 경우(조건 1)
                        return False
                    inclined[i+j] = True
                else: # 경사로를 놓다가 범위를 벗어나는 경우(조건 4)
                    return False

        else: # 오르막길인 경우
            target_2 = line[i] # 높은 지점의 칸 높이
            for j in range(l): # 경사로의 길이만큼 확인
                if 0 <= i-j < n:
                    if line[i-j] != target_2: # 낮은 지점의 칸의 높이가 모두 같지 않거나, L개가 연속되지 않은 경우(조건 3)
                        return False
                    if inclined[i-j]: # 경사로를 놓은 곳에 또 경사로를 놓는 경우(조건 1)
                        return False
                    inclined[i-j] = True
                else: # 경사로를 놓다가 범위를 벗어나는 경우(조건 4)
                    return False
            
    return True

for i in area:
    if checkLine(i):
        total += 1

for i in range(n):
    temp_area = []
    for j in range(n):
        temp_area.append(area[j][i])
    if checkLine(temp_area):
        total += 1

print(total)


# def checkRow(index): # 양쪽에서 모두 시작해야함
    
#     i = 0
#     k = n-1
    
#     while i < n:
#         if area[index][i] != area[index][i+1]:
#             if abs(area[index][i] - area[index][i+1]) >= 2: # 1. 현재 값과 다음 값이 다르고, 값의 차이가 2이상인 경우
#                 return False
#             for j in range(1,l+1):
#                 if area[index][i+j] != (area[index][i]-1) or visited[index][i+j]: # 2. 현재 값과 다음 값이 다르고, 길이 l 중에서 (현재 값-1)이 아니거나 이미 경사로가 깔린 경우
#                     return False
#             for j in range(1,l+1): # 경사로 깔기
#                 visited[index][i+j] = True

#         i += (l+1)

#     while k >= 0:
#         if area[index][k] != area[index][k-1]:
#             if abs(area[index][k] - area[index][k-1]) >= 2: # 1. 현재 값과 다음 값이 다르고, 값의 차이가 2이상인 경우
#                 return False
#             for j in range(1,l+1):
#                 if area[index][k-j] != (area[index][k]-1) or visited[index][k-j]: # 2. 현재 값과 다음 값이 다르고, 길이 l 중에서 (현재 값-1)이 아니거나 이미 경사로가 깔린 경우
#                     return False
#             for j in range(1,l+1): # 경사로 깔기
#                 visited[index][k-j] = True
#         k -= (l+1)

#     return True

# def checkColumn(index_2):
#     i = 0
#     k = n-1

#     is_available_row = True
#     is_available_col = True
    
#     while i < n-1:
#         if area[i][index_2] != area[i+1][index_2]:
#             if abs(area[i][index_2] - area[i+1][index_2]) >= 2: # 1. 현재 값과 다음 값이 다르고, 값의 차이가 2이상인 경우
#                 return False
#             for j in range(1,l+1):
#                 if i+j >= n-1:
#                     is_available_row = False
#                     break
#                 if area[i+j][index_2] != (area[i][index_2]-1) or visited[i+j][index_2]: # 2. 현재 값과 다음 값이 다르고, 길이 l 중에서 (현재 값-1)이 아니거나 이미 경사로가 깔린 경우
#                     is_available_row = False
#                     break

#             if is_available_row:
#                 for j in range(1,l+1): # 경사로 깔기
#                     visited[i+j][index_2] = True

#             i += (l+1)
#         else:
#             i += 1
        
#     if not is_available_row:
#         while k >= 0:
#             if area[k][index_2] != area[k-1][index_2]:
#                 if abs(area[k][index_2] - area[k-1][index_2]) >= 2: # 1. 현재 값과 다음 값이 다르고, 값의 차이가 2이상인 경우
#                     return False
#                 for j in range(1,l+1):
#                     if k-j < 0:
#                         is_available_col = False
#                         break
#                     if area[k-j][index_2] != (area[k][index_2]-1) or visited[k-j][index_2]: # 2. 현재 값과 다음 값이 다르고, 길이 l 중에서 (현재 값-1)이 아니거나 이미 경사로가 깔린 경우
#                         is_available_col = False
#                         break
#                 if is_available_col:
#                     for j in range(1,l+1): # 경사로 깔기
#                         visited[k-j][index_2] = True

#                 k -= (l+1)
#             else: 
#                 k -= 1

#     if not is_available_row and not is_available_col:
#         return False

#     return True

# for i in range(n):
#     print(checkRow(i))
#     if checkRow(i):
#         total += 1

# visited = [[False]*n for _ in range(n)]
# print()

# for i in range(n):
#     print(checkColumn(i))
#     if checkColumn(i):
#         total += 1

# print(total)
            
            
    

# 지나갈 수 없는 경우


# 3. 현재 값과 다음 값이 다르고 길이 l 이후에 값이 현재 값보다 크거나 같은 경우