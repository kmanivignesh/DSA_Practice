def count_neg_num(arr):
    l = 0
    r = len(arr) - 1
    first_neg =0 
    while l<=r:
        mid = (l + r)//2
        if arr[mid] < 0:
            first_neg = mid
            r =mid - 1
        else:
            l = mid + 1

    return len(arr) - first_neg

arr = [4,3,2,-1 , -2]
print(count_neg_num(arr))           