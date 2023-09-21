def solution(bridge_length, weight, truck_weights):
    time = 0
    
    queue = []
    
    while truck_weights or queue:
        
        time += 1
        
        if queue:
            queue = [(x[0],x[1]-1) for x in queue if x[1]-1 != 0]
        
        if truck_weights and sum([x[0] for x in queue]) + truck_weights[0] <= weight:
            v = truck_weights.pop(0)
            queue.append((v,bridge_length))
        
        
    return time