from itertools import combinations

def solution(dots):
    
    dots = [tuple(x) for x in dots]
    
    line_set = set([tuple(x) for x in dots])
    
    lines = list(combinations(dots,2))
    
    for line in lines:
        first_x, first_y = line[0][0], line[0][1]
        second_x, second_y = line[1][0], line[1][1]
        
        other_line = [x for x in line_set if x not in line]
        
        if len(other_line) == 0:
            return 1
        
        third_x, third_y = other_line[0][0], other_line[0][1]
        fourth_x, fourth_y = other_line[1][0], other_line[1][1]
        
        if ((first_y-second_y)/(first_x-second_x) == (third_y-fourth_y)/(third_x-fourth_x)):
            return 1
        
    return 0