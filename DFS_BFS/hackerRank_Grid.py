def bfs(x,y,area,row,column,visited):
    
    if area[x][y] != 1 or visited[x][y]:
        return 0
    
    count = 1
    visited[x][y] = True
    
    queue = [(x,y)]
     
    nx = [-1,1,0,0,-1,-1,1,1]
    ny = [0,0,-1,1,-1,1,-1,1]
    
    while queue:
        v = queue.pop(0)
        
        for i in range(8):
            temp_x = v[0] + nx[i]
            temp_y = v[1] + ny[i]
            
            if temp_x >= 0 and temp_x < row and temp_y >= 0 and temp_y < column:
                if area[temp_x][temp_y] == 1 and not visited[temp_x][temp_y]:
                    queue.append((temp_x,temp_y))
                    visited[temp_x][temp_y] = True
                    count += 1
                    
    return count
            
def connectedCell(matrix):
    # Write your code here
    
    row = len(matrix)
    column = len(matrix[0])
    
    visited = [[False]*column for _ in range(row)]
    
    max_value = 0
    
    for i in range(row):
        for j in range(column):
            value = bfs(i,j,matrix, row, column, visited)
            if value > max_value:
                max_value = value
                
    return max_value