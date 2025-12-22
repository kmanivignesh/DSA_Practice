#Leetcode - 26
def remove_duplicates(arr):
    i = 0
    for j in range(len(arr)):
        if arr[j] != arr[i]:
            i+=1
            arr[i] , arr[j] = arr[j] , arr[i]
    return arr[:(i+1)]

arr = [1 , 1 , 2 , 2 , 2 , 3 , 3 , 4 , 4 , 4 , 5]
print(remove_duplicates(arr))        