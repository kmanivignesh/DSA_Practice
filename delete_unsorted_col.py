def unsorted_count(arr):
    row = len(arr)
    col = len(arr[0])
    del_count = 0

    for i in range(col):
        for j in range(1 ,row):
            if arr[j-1][i] > arr[j][i]:
                del_count += 1
                break

    return del_count

