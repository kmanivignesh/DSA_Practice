def majority_element(arr):
    curr = arr[0]
    max = 1
    for i in range(1 , len(arr)):
        if curr == arr[i]:
            max+=1
        else:
            max -= 1

        if max == 0:
            curr = arr[i]
    return curr

arr = [ 1 , 1 , 2 , 2 , 4 , 4 , 4 , 4]
print(majority_element(arr))          