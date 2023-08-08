gear = [[0]*8 for _ in range(4)]
rotate_list = []

for i in range(4):
    gear[i] = list(map(int,list(input())))

def rotate_right(lst):
    lst.insert(0,lst.pop())

def rotate_left(lst):
    lst.append(lst.pop(0))    

k = int(input())

for i in range(k):
    number, direction = map(int,input().split())
    rotate_list.append((number-1,direction,"both"))

def rotate(n,direct,prop_direct):
    
    if n == 0: # 첫번째 기어일 경우
        if gear[n] != gear[n+1]: # 극이 다르면
            if direct == 1:
                rotate_list.append((n+1,-1,"right"))
            else:
                rotate_list.append((n+1,1,"right"))
        
        if direct == 1:
            rotate_right(gear[0])
        else:
            rotate_left(gear[0])

    # elif n == 1:
        
# gear = [[[0]*3 for _ in range(3)] for _ in range(4)]

# def rotate_90(matrix):
    
#     temp = [[0]*3 for _ in range(3)]
    
#     for i in range(3):
#         for j in range(3):
#             temp[j][3-i-1] = matrix[i][j]

#     return temp


# for i in range(4):
#     gear_status = list(map(int,list(input())))

#     gear[i][0][1] = gear_status[0]
#     gear[i][0][2] = gear_status[1]
#     gear[i][1][2] = gear_status[2]
#     gear[i][2][2] = gear_status[3]
#     gear[i][2][1] = gear_status[4]
#     gear[i][2][0] = gear_status[5]
#     gear[i][1][0] = gear_status[6]
#     gear[i][0][0] = gear_status[7]

# for i in gear:
#     for j in i:
#         print(j)
#     print()

# for i in range(4):
#     gear[i] = rotate_90(gear[i])

# for i in gear:
#     for j in i:
#         print(j)
#     print()

# # 