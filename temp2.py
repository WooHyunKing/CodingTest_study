# 자금세탁 감지 시스템
# 계좌의 주인 / 저번 달 거래 내역 / 이번 달 거래 내역

# 조건 1: 하루를 4시간으로 나눴을 때, 계좌의 주인이 저번 달 기준 가장 적은 거래 수를 기록한 시간에 거래가 발생한 경우
# 조건 2: 계좌의 주인이 저번 달 거래의 총액보다 큰 금액을 한 번에 거래한 경우

# 입력 : 계좌의 주인 이름 배열(owners), 지난 달 거래 내역(previous), 이번 달 거래 내역(now)
# 출력 : 이번 달 거래 내역 중에서 자극세탁 감지 시스템이 작동한 거래 

# 동명이인 X
# 같은 이름이 등장하면 한 사람이 여러 계좌를 가진 것
# 거래하는 두 계좌의 주인이 같은 경우는 X

# 00:00 ~ 03:59, 04:00 ~ 07:59, 08:00 ~ 11:59, 
# 12:00 ~ 15:59, 16:00 ~ 19:59, 20:00 ~ 23:59

def get_time(h,m):
    if 0 <= h <= 3:
        return 0
    elif 4 <= h <= 7:
        return 1
    elif 8 <= h <= 11:
        return 2
    elif 12 <= h <=15:
        return 3
    elif 16 <= h <= 19:
        return 4
    elif 20 <= h <= 23:
        return 5

owners = ["catch","olive","kitty","olive"]
previous = [[0,30,0,1,500],[23,12,2,3,1000],[8,0,0,2,100]]
now = [[7,10,1,0,1500],[12,30,2,3,2000]]

# owners = ['c','a','d','e','b']
# previous = [[14,19,2,1,200],[21,14,4,3,1500],[17,58,4,3,2900],[18,47,3,4,2700],[0,46,1,0,300],[12,57,0,1,2700],[7,48,2,4,1800],[9,20,0,1,2200],[8,41,3,0,3000],[23,31,3,0,2900]]
# now = [[3,53,2,4,900],[14,36,2,0,2000],[6,38,2,0,75100],[22,6,1,0,3800],[14,4,4,2,47700],[19,8,4,3,3300],[9,13,0,2,1400],[6,27,4,3,63800],[1,22,2,0,2000],[8,1,3,1,79200]]

person_dict = dict()
owner_total = dict()
time_count = [0]*6
time_table = dict()

answer = 0

for i, name in enumerate(owners):
    if i not in person_dict:
        person_dict[i] = name

for h, m, a, b, c in previous:
    
    time_index = get_time(h,m)

    if person_dict[a] not in time_table:
        time_table[person_dict[a]] = [0]*6
        time_table[person_dict[a]][time_index] += 1
    else:
        time_table[person_dict[a]][time_index] += 1

    if person_dict[b] not in time_table:
        time_table[person_dict[b]] = [0]*6
        time_table[person_dict[b]][time_index] += 1
    else:
        time_table[person_dict[b]][time_index] += 1

    if person_dict[a] not in owner_total:
        owner_total[person_dict[a]] = c
    else:
        owner_total[person_dict[a]] += c
    
    if person_dict[b] not in owner_total:
        owner_total[person_dict[b]] = c
    else:
        owner_total[person_dict[b]] += c

minimum_time_index = set([i for i,x in enumerate(time_count) if x == min(time_count)])

print(minimum_time_index) # {1, 3, 4}

for h, m, a, b, c in now:
    
    time_index = get_time(h,m)

    minimum_a = [i for i,x in enumerate(time_table[person_dict[a]]) if x == min(time_table[person_dict[a]])]
    minimum_b = [i for i,x in enumerate(time_table[person_dict[b]]) if x == min(time_table[person_dict[b]])]

    if time_index in minimum_a and owner_total[person_dict[a]] < c:
        answer += 1
        continue

    if time_index in minimum_b and owner_total[person_dict[b]] < c:
        answer += 1
        continue

print(answer)

    
    

