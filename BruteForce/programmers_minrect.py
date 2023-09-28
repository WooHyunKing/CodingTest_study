def solution(sizes):
    
    sizes = [sorted(x,reverse=True) for x in sizes]  # [[60, 50], [70, 30], [60, 30], [80, 40]]
    
    widths = [x[0] for x in sizes] # [60, 70, 60, 80]
    heights = [x[1] for x in sizes] # [50, 30, 30, 40]
    
    return max(widths)*max(heights)