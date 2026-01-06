def dfs(grid , x , y , oldcolor , newcolor):
    if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] != oldcolor:
        return 
    grid[x][y] = newcolor

    dfs(grid , x+1 , y , oldcolor , newcolor)
    dfs(grid , x-1 , y , oldcolor , newcolor)
    dfs(grid , x , y-1 , oldcolor , newcolor)
    dfs(grid , x , y-1 , oldcolor , newcolor)
    

def floodfill(grid , sr , sc  , newcolor):
    if grid[sr][sc] == newcolor:
        return
    
    dfs(grid , sr , sc , grid[sr][sc] , newcolor)
    return grid

    
    