def check_braces(Str):
    stack = []
    braces = {
        ']':'[',
        '}':'{',
        ')':'('
    }
    for i in Str:
        if i in '{({':
            stack.append(i)
        if i in braces and stack[-1] == braces[i]:
            stack.pop()
    return len(stack) == 0


Str = input("enter the String")
print(check_braces(Str))
                
        