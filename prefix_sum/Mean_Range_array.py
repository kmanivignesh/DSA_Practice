"""
Given an array arr[] of n integers and q queries represented by an array queries[][], 
where queries[i][0] = l and queries[i][1] = r. For each query, the task is to calculate the mean of elements 
in the range l to r and return its floor value.
"""
"""
Input: arr[] = [3, 7, 2, 8, 5] queries[][] = [[1, 3], [2, 5]]
Output: 4 5
Explanation: For query [1, 3] - Elements in range are 3, 7, 2
Mean is (3+7+2)/3 = 4, Floor value is 4
For query [2, 5] - Elements in range are 7, 2, 8, 5, 
Mean is (7+2+8+5)/4 = 5.5, Floor value is 5

Input: arr[] = [10, 20, 30, 40, 50, 60], queries[][] = [[4, 6]]
Output: 50
Explanation: For query [4, 6] - Elements in range are 40, 50, 60
Mean is (40+50+60)/3 = 50, Floor value is 50

"""


def prefix_sum(arr):
    prefix_sum = []
    prefix_sum.append(arr[0])
    for i in range(1 ,len(arr)):
        prefix_sum.append(arr[i] + prefix_sum[i-1])

    return prefix_sum

def range_mean(arr , queries):
    prefix_sum_array = prefix_sum(arr)
    mean = []
    for i in queries:
        sum = prefix_sum_array[i[1]-1] - prefix_sum_array[i[0]-1]
        total = i[1] - i[0]
        mean.append(sum //total)
    return mean    

if __name__ == "__main__":
    
    arr = [3, 7, 2, 8, 5]
    queries = [[1, 3], [2, 5]]
    
    print(range_mean(arr, queries))


