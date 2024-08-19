def solution(numbers, hand):
    answer = ''
    
    # 엄지손가락은 상하좌우 4가지 방향으로만 이동할 수 있으며 키패드 이동 한 칸은 거리로 1에 해당
    # 왼쪽 열의 3개의 숫자 1, 4, 7을 입력할 때는 왼손 엄지손가락을 사용
    # 오른쪽 열의 3개의 숫자 3, 6, 9를 입력할 때는 오른손 엄지손가락을 사용
    # 가운데 열의 4개의 숫자 2, 5, 8, 0을 입력할 때는 '두 엄지손가락의 현재 키패드의 위치에서 더 가까운 엄지손가락'을 사용
    # 만약 두 엄지손가락의 거리가 같다면 오른손잡이는 오른손 엄지손가락, 왼손잡이는 왼손 엄지손가락을 사용합니다.
    
    def calculate_distance(x, y, coor_d):
        return abs(coor_d[x][0]-coor_d[y][0])+abs(coor_d[x][1]-coor_d[y][1])
    
    area = [[1,2,3],[4,5,6],[7,8,9],['*',0,'#']]
    
    left_list, right_list = [1,4,7], [3,6,9]
    
    coor_d = dict()
    
    cl, cr = '*', '#'
    
    for i in range(4):
        for j in range(3):
            coor_d[area[i][j]] = (i,j)
    
    for n in numbers:
        if n in left_list:
            answer += 'L'
            cl = n
        elif n in right_list:
            answer += 'R'
            cr = n
        else:
            left_distance = calculate_distance(cl,n,coor_d)
            right_distance = calculate_distance(cr,n,coor_d)
            if left_distance < right_distance:
                answer += 'L'
                cl = n
            elif right_distance < left_distance:
                answer += 'R'
                cr = n
            else:
                if hand == 'left':
                    answer += 'L'
                    cl = n
                elif hand == 'right':
                    answer += 'R'
                    cr = n

    return answer