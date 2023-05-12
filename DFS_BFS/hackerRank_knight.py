#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'knightlOnAChessboard' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts INTEGER n as parameter.
#

def findMinimum(a,b,n):
    area = [[0]*n for _ in range(n)]
    visited = [[False]*n for _ in range(n)]
    nx = [a, a, -a, -a, b, b, -b, -b]
    ny = [b, -b, b, -b, a, -a, a, -a]
    queue =[[0,0]]
    
    visited[0][0] = True
    
    while queue:
        v = queue.pop(0)
        for i in range(8):
            temp_x = v[0] + nx[i]
            temp_y = v[1] + ny[i]
            
            if temp_x >= 0 and temp_x < n and temp_y >=0 and temp_y < n:
             if not visited[temp_x][temp_y]:
                if area[temp_x][temp_y] == 0:
                    area[temp_x][temp_y] = area[v[0]][v[1]] + 1
                else:
                    area[temp_x][temp_y] = min(area[temp_x][temp_y], area[v[0]][v[1]] + 1)
                queue.append([temp_x,temp_y])
                visited[temp_x][temp_y] = True
                
    if area[n-1][n-1] == 0:
        return -1
    else:
        return area[n-1][n-1]
            
    

def knightlOnAChessboard(n):
    # Write your code here
    result = [[0]*(n-1) for _ in range(n-1)]
    for i in range(1,n):
        for j in range(1,n):
            result[i-1][j-1]=findMinimum(i,j,n)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = knightlOnAChessboard(n)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
