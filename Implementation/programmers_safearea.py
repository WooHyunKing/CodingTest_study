def solution(board):
    
    # 지뢰가 있는 지역과 지뢰에 인접한 위, 아래, 좌, 우 대각선 칸을 모두 위험지역으로 분류
    # 지뢰는 2차원 배열 board에 1로 표시되어 있고 board에는 지뢰가 매설 된 지역 1과, 지뢰가 없는 지역 0만 존재
    
    answer = 0
    
    def return_boom_set(x,y):
        
        temp_set = set()
        
        for i in range(x-1,x+2):
            for j in range(y-1,y+2):
                if 0 <= i < n and 0 <= j < n:
                    temp_set.add((i,j))
                    
        return temp_set
    
    n = len(board)
    
    boom_set = set()
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                boom_set |= return_boom_set(i,j)
    
    for x, y in boom_set:
        board[x][y] = 1
    
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                answer += 1
                
    return answer