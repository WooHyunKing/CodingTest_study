def solution(participant, completion):
    
    dictionary = dict()
    
    for p in participant:
        if p not in dictionary:
            dictionary[p] = 1
        else:
            dictionary[p] += 1
    
    for c in completion:
        dictionary[c] -= 1
    
    for name, count in list(dictionary.items()):
        if count == 1:
            return name