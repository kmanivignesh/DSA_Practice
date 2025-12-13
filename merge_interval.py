def merge_array(arr):
    arr.sort(key = lambda x:x[0])
    merge_array = []
    merge_array.append(arr[0])
    for i in range(1 , len(arr)):
        if merge_array[-1][-1] < arr[i][0]:
            merge_array.append(arr[i])
        else:
            merge_array[-1][-1] = max(arr[i][-1] , merge_array[-1][-1])
    return merge_array        


interval = [[1 , 3] , [2 , 6] , [8 , 10] , [15 , 18]]
print(merge_array(interval))


    
    
        