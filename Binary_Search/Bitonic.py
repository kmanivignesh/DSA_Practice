#Now we wanna find a element which is where ther is an change means one side is strictly increasinf and other side is strictly decreasing

def bitonic_element(arr):
    l = 0
    r = len(arr) - 1
    while l<r:
        mid = l + (r - l)//2
        if arr[mid - 1] < arr[mid] and arr[mid] > arr[mid+1]:
            return mid
        elif arr[mid] > arr[mid - 1]:
            l = mid + 1
        else:
            r = mid
    return -1

arr = [1 , 4 , 5, 7 ,8 , 4 , 2 , 1]
print(bitonic_element(arr))