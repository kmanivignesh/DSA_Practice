def Except_itself_Product(arr):
    prod = 1
    num_zeros = 0
    ans = []
    for i in arr:
        if i == 0:
            num_zeros += 1
        else:
            prod *= i

    for i in arr:
        if num_zeros > 1:
            ans.append(0)
        elif num_zeros == 1:
            ans.append(prod if i == 0 else 0)
        else:
            ans.append(prod//i) 

    return ans

arr = [2 , 3 , 4 , 2 , 1]
print(Except_itself_Product(arr))
arr = [2 , 3 , 0 , 2 , 1]
print(Except_itself_Product(arr))
                           