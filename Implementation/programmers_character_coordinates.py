def solution(keyinput, board):
    answer = []
    # 게임에는 up, down, left, right 방향키가 있으며 각 키를 누르면 위, 아래, 왼쪽, 오른쪽으로 한 칸씩 이동
    # [0,0]에서 up을 누른다면 캐릭터의 좌표는 [0, 1], down을 누른다면 [0, -1], left를 누른다면 [-1, 0], right를 누른다면 [1, 0]
    
    # 방향키의 배열 keyinput와 맵의 크기 board
    
    # 캐릭터는 항상 [0,0]에서 시작
    
    # 키 입력이 모두 끝난 뒤에 캐릭터의 좌표 [x, y]를 return
    
    left_min, right_max = -board[1]//2+1, board[1]//2
    up_min, down_max = -board[0]//2+1, board[0]//2
    
    x, y = 0, 0
    
    for key in keyinput:

        if key == 'up' and y+1 <= right_max:
            y += 1
        elif key == 'down' and y-1 >= left_min:
            y -= 1
        elif key == 'left' and x-1 >= up_min:
            x -= 1
        elif key == 'right' and x+1 <= down_max:
            x += 1
    
    return [x,y]