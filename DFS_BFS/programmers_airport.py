def solution(tickets):
    answer = []
    graph = {}
    
    for i in range(len(tickets)):
        if tickets[i][0] not in graph:
            graph[tickets[i][0]] = [tickets[i][1]]
        else:
            graph[tickets[i][0]].append(tickets[i][1])
            graph[tickets[i][0]].sort(reverse=True)
            
    print(graph)
    
    stack = ["ICN"]
    
    while stack:
        top = stack[-1]
        
        if top not in graph or not graph[top]:
            print("stack pop : ",stack[-1])
            answer.append(stack.pop())
        else:
            print("graph top pop : ",graph[top][-1])
            stack.append(graph[top].pop())
                
    return answer[::-1]