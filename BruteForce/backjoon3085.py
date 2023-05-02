n = int(input())

array = [[] for _ in range(n)]

nx = [-1,1,0,0]
ny = [0,0,-1,1]

for i in range(n):
    array[i] = list(input())

# 행에서 연속된 문자의 개수를 확인하는 함수
def row_check(x,y):
    count = 1
    for i in range(y,n+1):
        if i == n-1:
            break
        if array[x][i] == array[x][i+1]:
            count += 1
        else:
            break

    for i in range(y,-1,-1):
        if i == 0:
            break
        if array[x][i] == array[x][i-1]:
            count += 1
        else:
            break
    return count

# 열에서 연속된 문자의 개수를 확인하는 함수
def col_check(x,y):
    count = 1
    for i in range(x,n+1):
        if i == n-1:
            break
        if array[i][y] == array[i+1][y]:
            count += 1
        else:
            break
    for i in range(x,-1,-1):
        if i == 0:
            break
        if array[i][y] == array[i-1][y]:
            count += 1
        else:
            break
    return count

max_value = 0

for i in range(n):
    for j in range(n):
        copy_array = array

        if max(row_check(i,j), col_check(i,j)) > max_value:
            max_value = max(row_check(i,j), col_check(i,j))
        
        for k in range(4):
            temp_x = i + nx[k]
            temp_y = j + ny[k]

            if temp_x >=0 and temp_x < n and temp_y >=0 and temp_y < n:

                copy_array[i][j], copy_array[temp_x][temp_y] = copy_array[temp_x][temp_y], copy_array[i][j]
                
                if max(row_check(i,j), col_check(i,j)) > max_value:
                    max_value = max(row_check(i,j), col_check(i,j))

                copy_array[i][j], copy_array[temp_x][temp_y] = copy_array[temp_x][temp_y], copy_array[i][j]
print(max_value)