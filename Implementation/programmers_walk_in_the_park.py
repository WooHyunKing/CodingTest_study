def solution(park, routes):
    
    # 지나다니는 길을 'O', 장애물을 'X'
    # 1. 주어진 방향으로 이동할 때 공원을 벗어나는지 확인
    # 2. 주어진 방향으로 이동 중 장애물을 만나는지 확인

    area = []
    
    for i in park:
        area.append(list(i))
        
    w, h = len(area[0]), len(area)
    
    for i in range(h):
        for j in range(w):
            if area[i][j] == 'S':
                cx, cy = i, j
    
    def check(area, x, y, d, n):
        
        if d == 'N':
            if x-n < 0:
                return False
            for i in range(1, n+1):
                if area[x-i][y] == 'X':
                    return False
        elif d == 'S':
            if x+n >= h :
                return False
            for i in range(1, n+1):
                if area[x+i][y] == 'X':
                    return False
        if d == 'W':
            if y-n < 0:
                return False
            for i in range(1, n+1):
                if area[x][y-i] == 'X':
                    return False
        if d == 'E':
            if y+n >= w:
                return False
            for i in range(1, n+1):
                if area[x][y+i] == 'X':
                    return False
        return True
    
    for route in routes:
        d, n = route.split()
        
        if not check(area,cx,cy,d,int(n)):
            continue
        
        if d == 'N':
            cx -= int(n)
        elif d == 'S':
            cx += int(n)
        elif d == 'W':
            cy -= int(n)
        elif d == 'E':
            cy += int(n)
        
    return [cx,cy]