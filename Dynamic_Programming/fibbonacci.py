def fibonacci_bottom_up(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    A = [0]*(num+1)
    A[0] , A[1] = 0 , 1
    for i in range(2 , num+1):
        A[i] = A[i-1] + A[i-2]

    return A[num]

num = int(input("Enter the number : "))
print(fibonacci_bottom_up(num))    