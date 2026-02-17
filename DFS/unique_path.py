def count_unique_path(m , n):
    grid = [[0]*n for _ in range(m)]
    def dfs(grid , i , j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
            return 0
        if i == len(grid) - 1 and j == len(grid[0]) - 1:
            return 1
        return dfs(grid , i + 1 , j) + dfs(grid , i , j + 1)

    return dfs(grid , 0 , 0)

m = int(input("Enter the m : "))
n = int(input("Enter the n : "))
print(count_unique_path(m , n))

    