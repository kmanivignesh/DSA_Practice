def construct_parenthesis(n):
    result = []
    def dfs(curr , open , closed):
        if len(curr) == n:
            result.append(curr)
        if open < n:
            dfs(curr + '(' , open + 1 , closed)
        if closed < open:
            dfs(curr + ')' , open , closed + 1)
    dfs('',0,0)
    return result

n = int(input("Enter the number : "))
print(construct_parenthesis(n))
                