def search_soreted_matrix(matrix , target):
    n = len(matrix)
    m = len(matrix[0])

    l = 0
    r = m*n - 1
    while l <= r:
        mid = l + (r - l)//2
        row = mid//n
        col = mid%n
        print(mid , ' ' , row ,' ',col , ' ',matrix[row][col])
        if matrix[row][col] == target:
            return row,col
        elif matrix[row][col] > target:
            r = mid - 1
        else:
            l = mid + 1
    return -1

matrix = [[1 , 2, 3 , 4] ,
          [5 , 6 , 7 ,8] ,
          [9 , 10 ,11 ,12],
          [13 , 14 , 15 , 16]]

print(search_soreted_matrix(matrix , 5))            

