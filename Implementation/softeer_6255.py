import sys
from collections import deque

input = sys.stdin.readline

# 플레이페어 암호는 알파벳으로 이루어진 어떤 문자열을 암호화하는 방법
# 알파벳으로 이루어진 문자열인 Key가 필요함
# 한번에 두 글자 단위로 암호화를 진행
# 5x5 크기의 표를 사용, 알파벳 26개를 모두 담기에는 칸이 1개 부족하여 I와 J를 동일하게 생각(편의상 J가 아예 X)

# 1. 주어진 키를 5x5 크기의 표로 변환
# 키를 한 글자씩 보면서 왼쪽 위 칸부터 한줄씩 표를 채운다. 만약 이전에 봤던 알파벳이 한번 더 등장하면 무시하고 다음 글자를 본다.
# 키를 다 보고도 칸이 남는다면, 아직 등장하지 않은 알파벳을 순서대로 채워넣는다.

# 2. 암호화하려는 메세지를 두 글자씩 나눈다.
# 같은 두글자로 쌍을 이루면 그중 가장 앞에 있는 쌍 사이에 X를 넣고 뒤쪽에는 쌍을 새롭게 쌍을 구성
# 만약에 쌍이 XX라면 Q를 넣어서 해결
# 이렇게 쌍을 모두 맞추고 마지막에 한 글자가 남는다면 여기도 X를 덧붙여 쌍을 맞춰준다.
# 마지막 남은 한 글자가 X인 경우에는 예외적으로 XX로 쌍을 맞춘다.

area = [['']* 5 for _ in range(5)]

alpa = [chr(x) for x in range(ord('A'),ord('Z')+1) if x != ord('J')]
alpa_set = set()

message = deque(list(input().rstrip()))
key = deque(list(input().rstrip()))

twice_list = []

def one():

    i, j = 0, 0

    while key and 0 <= i < 5 and 0 <= j < 5:
        v = key.popleft()

        if v not in alpa_set:
            alpa_set.add(v)
            area[i][j] = v
            j += 1
            if j >= 5:
                i += 1
                j = 0
            if i >= 5:
                break
                
    for c in alpa:
        if c not in alpa_set:
            # alpa_set.add(c)
            area[i][j] = c
            j += 1
            if j >= 5:
                i += 1
                j = 0
            if i >= 5:
                break
        
one()

def two():
    
    temp = ''

    while message:

        v = message.popleft()

        if len(temp) == 0:
            temp += v
        elif len(temp) == 1:
            if temp == v:
                if temp == "X" and v == "X":
                    temp += "Q"
                else:
                    temp += 'X'
                twice_list.append(temp)
                message.appendleft(v)
            else:
                temp += v
                twice_list.append(temp)
            temp = ""
    if temp != "":
        twice_list.append(temp+"X")

two()

def check_row(i,first,second):
    temp = "".join(area[i]) 
    if first in temp and second in temp:
        return True
    else:
        return False

def check_col(i,first,second):
    temp = ""
    for t in range(5):
        temp += area[t][i]
    if first in temp and second in temp:
        return True
    else:
        return False 

def check_in_row(i,value):
    temp = "".join(area[i])
    if value in temp:
        return True
    else:
        return False

def check_in_col(i,value):
    temp = ""
    for t in range(5):
        temp += area[t][i]
    if value in temp:
        return True
    else:
        return False

def three():

    for ti,twice in enumerate(twice_list):
        fb, sb = False, False
        for i in range(5):   
            if check_row(i,twice[0],twice[1]):
                temp = "".join(area[i]) 
                first_index, second_index = temp.find(twice[0]), temp.find(twice[1])
                twice_list[ti] = area[i][(first_index + 1) %5] + area[i][(second_index + 1) %5]
                fb = True
                break
        if fb:
            continue

        for i in range(5):
            if check_col(i,twice[0],twice[1]):
                temp = ""
                for t in range(5):
                    temp += area[t][i]
                first_index, second_index = temp.find(twice[0]), temp.find(twice[1])
                twice_list[ti] = area[(first_index+1)%5][i] + area[(second_index+1)%5][i]
                sb = True 
        if sb:
            continue

        first_col, second_col = -1, -1

        for i in range(5):
            if check_in_col(i,twice[0]):
                first_col = i
            if check_in_col(i,twice[1]):
                second_col = i
            if check_in_row(i,twice[0]):
                first_row = i
            if check_in_row(i,twice[1]):
                second_row = i
        if first_col == -1 or second_col == -1:
            continue
        else:
            twice_list[ti] = area[first_row][second_col] + area[second_row][first_col]

three()

print("".join(twice_list))