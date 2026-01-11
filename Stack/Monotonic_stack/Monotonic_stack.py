def monotonic_stack(arr):
    stack = []
    m = len(arr)
    result = [-1]*m
    for i in range(m):
        print(i)
        while len(stack)!=0 and arr[stack[-1]] < arr[i]:
            result[stack.pop()] = arr[i]
        stack.append(i) 
    return result

arr = [2 , 1 , 5 , 6 , 2 , 3]
print(monotonic_stack(arr))       
