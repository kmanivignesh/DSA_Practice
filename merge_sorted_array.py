def mearge_sorted_array(arr1,arr2):
    i,j = 0 ,0 
    new_arr = []
    while(i < len(arr1) and j < len(arr2)):
        if arr1[i] < arr2[j]:
            new_arr.append(arr1[i])
            i+=1
        else:
            new_arr.append(arr2[j])
            j+=1
    while i < len(arr1):
        new_arr.append(arr1[i])
        i+=1
    while j < len(arr2):
        new_arr.append(arr2[j])
        j+=1

    return new_arr

arr1 = [1,3,5,7]
arr2 = [2,4,6]
print(mearge_sorted_array(arr1,arr2))






        