def countLuck(matrix, k):
    
    row = len(matrix)
    col = len(matrix[0])
    nx = [-1,1,0,0]
    ny = [0,0,-1,1]
    start_x, start_y = 0, 0
    
    count = 0
    
    graph = []
    for i in range(row):
        graph.append(list(matrix[i]))
    
    for i in range(row):
        for j in range(col):
            if graph[i][j] == 'M':
                start_x, start_y = i, j
    
    # Write your code here
    def dfs(area, x, y):
        # visited[x][y] = True
        
        if area[x][y] == '*':
            return True
            
        direct_count = 0
        
        for i in range(4):
            temp_x = x + nx[i]
            temp_y = y + ny[i]
            
            if temp_x >=0 and temp_x < row and temp_y >=0 and temp_y < col:
                if area[temp_x][temp_y] == '.' or area[temp_x][temp_y] == '*':
                    direct_count += 1
                    
        if direct_count > 1:
            area[x][y] = '1'
        else:
            area[x][y] = '0'
            
        for i in range(4):
            temp_x = x + nx[i]
            temp_y = y + ny[i]
            
            if temp_x >=0 and temp_x < row and temp_y >=0 and temp_y < col:
                if area[temp_x][temp_y] == '.' or area[temp_x][temp_y] == '*':
                     if dfs(area,temp_x,temp_y):
                        return True
        area[x][y] = '.'
        
        return False
            
    dfs(graph,start_x,start_y)
    
    for i in range(row):
        for j in range(col):
            if graph[i][j] == '1':
                count += 1
    
    if count == k:
        return "Impressed"
    else:
        return "Oops!"