# H - 앞, T - 뒷

# 모두 같은 면을 보이도록 한다
# 한 행이나 한 열의 모든 동전, 또는 대각선의 모든 동전을 한번에 뒤집어야 함

# 최소 횟수의 연산으로 모든 면이 같도록 만든다

# 모두 같은 면이 보이도록 하는 최소 연산 횟수, 불가능하면 -1

from collections import deque

t = int(input())


def reverse_row(area, index):
    temp = [item[:] for item in area]
    for i in range(3):
        if area[index][i] == "H":
            temp[index][i] = "T"
        elif area[index][i] == "T":
            temp[index][i] = "H"
    return temp

def reverse_col(area,index):
    temp = [item[:] for item in area]
    for i in range(3):
        if area[i][index] == "H":
            temp[i][index] = "T"
        elif area[i][index] == "T":
            temp[i][index] = "H"
    return temp

def reverse_cross(area):
    temp = [item[:] for item in area]
    for i in range(3):
        if area[i][i] == "H":
            temp[i][i] = "T"
        elif area[i][i] == "T":
            temp[i][i] = "H"
    return temp

def reverse_cross_two(area):
    temp = [item[:] for item in area]
    for i in range(3):
        if area[i][2-i] == "H":
            temp[i][2-i] = "T"
        elif area[i][2-i] == "T":
            temp[i][2-i] = "H"
    return temp

def check_all_same(area):
    
    first = area[0][0]

    for i in range(3):
        for j in range(3):
            if area[i][j] != first:
                return False
            
    return True

for _ in range(t):
    area = [list(input().split()) for _ in range(3)]
    
    def bfs():
        visited_row = [False for _ in range(3)]
        visited_col = [False for _ in range(3)]
        visited_cross = False
        visited_cross_two = False
        
        queue = deque([(area,0,visited_row,visited_col,visited_cross,visited_cross_two)])

        while queue:
            
            v, count, visited_r, visited_c, visited_cross, visited_cross_two = queue.popleft()

            if check_all_same(v):
                print(count)
                return
            
            for i in range(3):
                if not visited_r[i]:
                    temp_visited_r = visited_r[:]
                    temp_visited_r[i] = True
                    new_area = reverse_row(v,i)
                    queue.append((new_area,count+1,temp_visited_r,visited_c, visited_cross, visited_cross_two))
            
            for i in range(3):
                if not visited_c[i]:
                    temp_visited_c = visited_c[:]
                    temp_visited_c[i] = True
                    new_area = reverse_col(v,i)
                    queue.append((new_area,count+1,visited_r,temp_visited_c, visited_cross, visited_cross_two))
            
            if not visited_cross:
                new_area = reverse_cross(v)
                queue.append((new_area,count+1,visited_r,visited_c,not visited_cross,visited_cross_two))
            if not visited_cross_two:
                new_area = reverse_cross_two(v)
                queue.append((new_area,count+1,visited_r,visited_c,visited_cross,not visited_cross_two))
                
        print(-1)

        return

    bfs()