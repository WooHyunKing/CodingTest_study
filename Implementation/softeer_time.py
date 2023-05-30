import sys

t = int(input())

def set_time(n):
    time = [0]*7

    if n == 0:
        time[0],time[1],time[2],time[4],time[5],time[6] = 1,1,1,1,1,1
    elif n == 1:
        time[2],time[5] = 1,1
    elif n == 2:
        time[0],time[2],time[3],time[4],time[6] = 1,1,1,1,1
    elif n == 3:
        time[0],time[2],time[3],time[5],time[6] = 1,1,1,1,1
    elif n == 4:
        time[1],time[2],time[3],time[5] = 1,1,1,1
    elif n == 5:
        time[0],time[1],time[3],time[5],time[6] =1,1,1,1,1
    elif n == 6:
        time[0],time[1],time[3],time[4],time[5],time[6] = 1,1,1,1,1,1
    elif n == 7:
        time[0],time[1],time[2],time[5] = 1,1,1,1
    elif n == 8:
        time[0],time[1],time[2],time[3],time[4],time[5],time[6] = 1,1,1,1,1,1,1
    elif n == 9:
        time[0],time[1],time[2],time[3],time[5],time[6] = 1,1,1,1,1,1

    return time

for _ in range(t):
    a,b = input().split()

    time_list_a = [[0]*7 for _ in range(5)]
    time_list_b = [[0]*7 for _ in range(5)]
    
    len_a = len(a)
    len_b = len(b)

    for i in range(len_a):
        time_list_a[4-i] = set_time(int(a[len_a-1-i]))
    
    for i in range(len_b):
        time_list_b[4-i] = set_time(int(b[len_b-1-i]))

    result = 0
    
    for i in range(5):
        count = 0
        for j in range(7):
            diff = abs(time_list_a[i][j] - time_list_b[i][j])
            count += diff
        result += count
    
    print(result)