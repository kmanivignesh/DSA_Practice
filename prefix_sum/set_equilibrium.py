def find_equilibrium_app1(arr):
    n = len(arr) - 1
    prefix_array = [0]*(n+1)
    prefix_array[0] = arr[0]
    suffix_array = [0]*(n+1)
    suffix_array[n] = arr[n]
    for i in range(1 , len(arr)):
        prefix_array[i] = arr[i] + prefix_array[i-1]
    for i in range(len(arr) - 2 , 0 , -1):
        suffix_array[i] =  arr[i] + suffix_array[i+1]


    for i in range(len(arr)):
        if suffix_array[i] == prefix_array[i]:
            return i
    return -1

def find_equlibrium_app2(arr):
    sum = 0
    for i in range(len(arr)):
        sum+= arr[i]
    prefix_sum = 0
    for i in range(len(arr)):
        suffsum = sum - prefix_sum - arr[i]
        if suffsum == prefix_sum:
            return i
        prefix_sum+=arr[i]
        
        

if __name__ == "__main__":
    arr = [-7, 1, 5, 2, -4, 3, 0]

    print(find_equilibrium_app1(arr))
    print(find_equlibrium_app2(arr))    

        