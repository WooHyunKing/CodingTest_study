bingo = [list(map(int,input().split())) for _ in range(5)]

numbers = []

answer = 0

for i in range(5):
    numbers += list(map(int,input().split()))

def delete_number(n):
    for i in range(5):
        for j in range(5):
            if bingo[i][j] == n:
                bingo[i][j] = 0
                return

def count_row(): # 5개가 지워진 행의 개수
    count = 0
    for i in range(5):
        if sum(bingo[i]) == 0:
            count += 1
    return count

def count_col(): # 5개가 지워진 열의 개수
    count = 0
    for i in range(5):
        total = 0
        for j in range(5):
            total += bingo[j][i]
        if total == 0:
            count += 1
    return count

def count_dig(): # 5개가 지워진 대각선의 개수
    count = 0
    if sum([bingo[x][x] for x in range(5)]) == 0:
        count += 1
    if sum([bingo[x][4-x] for x in range(5)]) == 0:
        count += 1
    
    return count

for num in numbers:
    if (count_row() + count_col() + count_dig()) >= 3:
        break

    delete_number(num)

    answer += 1

print(answer)