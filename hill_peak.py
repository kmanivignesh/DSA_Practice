def peak_hill(arr):
    if len(arr) == 1:
        return arr
    i = 1
    j = len(arr) - 2
    while i <= j:
        mid = (i+j)//2
        if arr[mid] > arr[mid+1] and arr[mid] > arr[mid - 1]:
            return arr[mid]
        elif arr[mid] <arr[mid+1]:
            i = i + 1
        else:
            j = j - 1

    return -1

mountain = [1,2,3,9,5,6,2]   
print(peak_hill(mountain))     

    