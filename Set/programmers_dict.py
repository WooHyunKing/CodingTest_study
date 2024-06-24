from itertools import permutations

def solution(spell, dic):
    
    dic_set = set(dic)
    
    cases = ["".join(list(x)) for x in list(permutations(spell,len(spell)))]
    
    for case in cases:
        if case in dic_set:
            return 1
    
    return 2