t = int(input())

answer = []

def special_sort(arr):

    get_min = False
    
    for i in range(len(arr)):
        if get_min:
            min_index = i
            for j in range(i+1,len(arr)):
                if arr[min_index] > arr[j]:
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]
        else:
            max_index = i
            for j in range(i+1,len(arr)):
                if arr[max_index] < arr[j]:
                    max_index = j
            arr[i], arr[max_index] = arr[max_index], arr[i]
        
        get_min = not get_min
    
    return arr[:10]
        

for _ in range(t):
    n = int(input())

    data = list(map(int,input().split()))

    answer.append(special_sort(data))

for i,value in enumerate(answer):
    result = " ".join(str(s) for s in value)
    print(f"#{i+1} {result}")