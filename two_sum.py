def two_sum(arr , target):
    sum_dict = {}
    for i in range(len(arr)):
        temp = target - arr[i]
        print(temp)

        if arr[i] in sum_dict:
            return sum_dict[arr[i]] , i
        else:
            sum_dict[temp] = i
            print(sum_dict)
    return -1

arr = [23 , 21 , 12 , 14 , 17 , 29]        
print(two_sum(arr , 37))