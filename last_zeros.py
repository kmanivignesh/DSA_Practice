import math

def last_zeros(arr):
    left = 0
    for right in range(len(arr)):
        if arr[right] != 0:
            arr[right],arr[left] = arr[left],arr[right]
            left += 1

    return arr        

    

def is_prime(num):
    for i in range(2,int(num**(0.5))):
        if num%i == 0:
            return False
    return True    



if __name__=="__main__":
    arr = [1,0,0,1,2,0,3,2]
    # a = int(input("Enter the number : "))
    print(last_zeros(arr))        