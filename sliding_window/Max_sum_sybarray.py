def max_sum(arr ,k):
    if len(arr)-1 < k:
        return
    sum = 0
    for i in range(k):
        sum+= arr[i]
    long = sum
    for i in range(k , len(arr)):
        sum+= arr[i] - arr[i-k]
        long= max(sum , long)
    return long

if __name__ == "__main__":
    arr = [5, 2, -1, 0, 3]
    k = 3
    n = len(arr)
    print(max_sum(arr, k))    
            
