def solution(s):
    bin_count, zero_count = 0, 0
    
    while s != "1":

        zero_count += s.count("0")
        
        s = bin(len("".join([x for x in s if x != "0"]))).split("b")[1]
        
        bin_count += 1
        
    return [bin_count,zero_count]