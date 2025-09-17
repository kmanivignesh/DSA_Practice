def common_prefix(arr):
    prefix = arr[0]
    for i in arr[1:]:
        while i[:len(prefix)] != prefix:
            prefix = prefix[:-1]
            if not prefix:
                return True
            
    return prefix

words = ["flower", "flow", "flight"]
print("Longest Common Prefix:", common_prefix(words))
   