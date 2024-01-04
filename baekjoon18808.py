n, m, k = map(int,input().split())

paper = [[0]*m for _ in range(n)]

count = 0

for _ in range(k):
    r,c = map(int,input().split())

    sticker = [list(map(int,input().split())) for _ in range(r)]

    def check_available(paper,x,y,sticker,sticker_row_len,sticker_col_len):
        for i in range(sticker_row_len):
            for j in range(sticker_col_len):
                if sticker[i][j] == 1 and paper[x+i][y+j] == 1:
                    return False
        return True
    
    def add_area(paper,x,y,sticker,sticker_row_len,sticker_col_len):
        temp_paper = [item[:] for item in paper]
        for i in range(sticker_row_len):
            for j in range(sticker_col_len):
                if sticker[i][j] == 1:
                    temp_paper[x+i][y+j] = 1
        return temp_paper
    
    def rotate(sticker):
        row_len = len(sticker)
        col_len = len(sticker[0])

        new_sticker = [[0]*row_len for _ in range(col_len)]

        for i in range(row_len):
            for j in range(col_len):
                new_sticker[j][row_len-1-i] = sticker[i][j]
        
        return new_sticker
        
    
    def paint(sticker):
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

    if paint(sticker):
        continue

    for _ in range(3):
        sticker = rotate(sticker)
        if paint(sticker):
            break

for i in range(n):
    for j in range(m):
        if paper[i][j] == 1:
            count += 1

print(count)