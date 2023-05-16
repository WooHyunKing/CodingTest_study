def insertionSort1(n, arr):
    # Write your code here
    for i in range(n-1,0,-1):
        if arr[i] < arr[i-1]:
            new_array = arr.copy()
            new_array[i] = arr[i-1]
            
            for j in new_array:
                print(j, end=" ")
            print()
                
            arr[i], arr[i-1] = arr[i-1], arr[i]
            
            if i == 1:
                for j in arr:
                    print(j, end=" ")
            
        else:
            for j in arr:
                print(j, end=" ")
            break