def Merge_Interval(arr):
    arr.sort(key = lambda x : x[0])
    final_arr = []
    final_arr.append(arr[0])
    for i in range(1 , len(arr)):
        if arr[i][0] <= final_arr[-1][-1]:
            final_arr[-1][-1] = max(arr[i][-1] , final_arr[-1][-1])
        else:
            final_arr.append(arr[i])
    return final_arr

arr = [[8,10] , [13,16] , [2,5] , [0,3] , [4,6] , [10,11] ]
print(Merge_Interval(arr))