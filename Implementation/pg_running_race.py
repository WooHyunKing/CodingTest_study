def solution(players, callings):
    
    # {'mumu': 0, 'soe': 1, 'poe': 2, 'kai': 3, 'mine': 4}
    player_dict = {player:rank for rank,player in enumerate(players)}
    # {0: 'mumu', 1: 'soe', 2: 'poe', 3: 'kai', 4: 'mine'}
    rank_dict = {rank:player for rank,player in enumerate(players)}
    
    for call in callings:
        call_index = player_dict[call]
        prev_index = call_index -1
        
        player_dict[rank_dict[call_index]], player_dict[rank_dict[prev_index]] = prev_index, call_index
        rank_dict[call_index], rank_dict[prev_index] = rank_dict[prev_index], rank_dict[call_index]
        
    return list(rank_dict.values())