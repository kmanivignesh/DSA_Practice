"""
Given a listof daily temperatures determine how many days you will have to wait for a warmer day
will have to wait for an warmer day

input : [73 , 74 , 75 , 71 , 69 , 72 , 76 , 73]
output : [1 , 1 , 1 , 4 , 0 ,0]
"""

def wait_warmer_day(temperatures):
    n = len(temperatures)
    stack = []
    result = [0]*n
    count = 0
    for i in range(n):
        
        while len(stack) != 0 and temperatures[stack[-1]] < temperatures[i]:
            prev_index = stack.pop()
            result[prev_index] = i - prev_index
        stack.append(i)
    return result

temperatures = [73 , 74 , 75 , 71 , 69 , 72 , 76 , 73]
print(wait_warmer_day(temperatures))      

