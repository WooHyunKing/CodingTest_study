n, m, k = map(int,input().split())

paper = [[0]*m for _ in range(n)]

count = 0

for _ in range(k):
    r,c = map(int,input().split())

    sticker = [list(map(int,input().split())) for _ in range(r)]

    def check_available(paper,x,y,sticker,sticker_row_len,sticker_col_len): # 스티커를 붙일 수 있는지 확인하는 함수
        for i in range(sticker_row_len):
            for j in range(sticker_col_len):
                if sticker[i][j] == 1 and paper[x+i][y+j] == 1:
                    return False
        return True
    
    def add_area(paper,x,y,sticker,sticker_row_len,sticker_col_len): # 스티커를 붙이는 함수
        temp_paper = [item[:] for item in paper]
        for i in range(sticker_row_len):
            for j in range(sticker_col_len):
                if sticker[i][j] == 1:
                    temp_paper[x+i][y+j] = 1
        return temp_paper
    
    def rotate(sticker): # 2차원 배열을 90도 회전시키는 함수
        row_len = len(sticker)
        col_len = len(sticker[0])

        new_sticker = [[0]*row_len for _ in range(col_len)]

        for i in range(row_len):
            for j in range(col_len):
                new_sticker[j][row_len-1-i] = sticker[i][j]
        
        return new_sticker
        
    
    def paint(sticker): # 종이에 스티커를 붙이기 위해 모든 경우의 수를 시도하는 함수(성공하면 true 반환)
        global paper
        for i in range(n):
            for j in range(m):
                sticker_row_len = len(sticker)
                sticker_col_len = len(sticker[0])

                if 0 <= (i + sticker_row_len -1) < n and 0 <= (j + sticker_col_len -1) <  m:
                    if check_available(paper,i,j,sticker,sticker_row_len,sticker_col_len):
                        paper = add_area(paper,i,j,sticker,sticker_row_len,sticker_col_len)
                        return True
        return False

    if paint(sticker): # 종이에 바로 스티커를 붙이는데 성공하면 바로 다음 스티커로 continue
        continue

    for _ in range(3): # 90도 회전하면서 스티커를 붙일 수 있는지 확인, 붙이는데 성공하면 break
        sticker = rotate(sticker)
        if paint(sticker):
            break

for i in range(n):
    for j in range(m):
        if paper[i][j] == 1:
            count += 1

print(count)