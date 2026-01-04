def square_root(num):
    l , r = 0 , num
    while l <= r:
        mid = l + (r - l)//2
        if mid*mid == num:
            return mid
        elif mid*mid < num:
            l = mid + 1
        else:
            r = mid - 1 
    return r

num = int(input("Enter the number : "))
print(square_root(num))

           