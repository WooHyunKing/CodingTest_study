def solution(name, yearning, photo):
    answer = []
    
    # 	{'may': 5, 'kein': 10, 'kain': 1, 'radi': 3}
    name_dict = {name:yearning[i] for i,name in enumerate(name)}
    
    for i,row in enumerate(photo):
        total = 0
        for j,col in enumerate(row):
            if name_dict.get(col) != None:
                total += name_dict[col]
        answer.append(total)
            
    return answer