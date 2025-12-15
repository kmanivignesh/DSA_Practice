def longest_consecutive_seq(arr):
    seen = set(arr)
    longest = 0
    for i in range(len(arr)):
        if arr[i]-1 not in seen:
            curr = arr[i]
            temp = 0
            while curr in arr:
                temp += 1
                curr+=1
            longest = max(longest , temp)

    return longest

arr = [14 , 5 , 6 , 7 , 4 , 3, 2]
print(longest_consecutive_seq(arr))