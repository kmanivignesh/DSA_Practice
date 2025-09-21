def gcd(a,b):
    
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

def lcm(a,b):
    if a == 0 or b== 0:
        return 0
    return a*b//gcd(a,b)

def isprime(a):
    ans = ['even','odd']
    return ans[a%2]

def print_sub(str,num):
    if num == 0:
        return 
    else:
        print(str)
        print_sub(str,num-1)

a = input("Enter the string : ")
b = int(input("Enter the count : "))
print_sub(a,b)
