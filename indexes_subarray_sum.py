#Amazon , Facebook ,Google , Visa

def subarray_sum(arr , target):
    i = 0
    sum = arr[0]
    for j in range(1,len(arr)):
        
        while sum >= target:
            if sum == target:
                return i,j

            sum -= arr[i]
            i += 1
        sum+=arr[j]
    return -1

arr = [1 , 2 , 3 , 7 , 5]
target = 12
print(subarray_sum(arr , target))



