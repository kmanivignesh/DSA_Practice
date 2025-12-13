def find_target(matrix, target):
    r = len(matrix)
    c = len(matrix[0])

    left = 0
    right = r * c - 1

    while left <= right:
        mid = (left + right) // 2
        row = mid // c
        col = mid % c

        if matrix[row][col] == target:
            return True
        elif target < matrix[row][col]:
            right = mid - 1
        else:
            left = mid + 1

    return False
