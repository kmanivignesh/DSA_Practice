def is_happy_num(num):
    seen = set()
    while num not in seen and num != 1:
        seen.add(num)
        num = sum([int(i)**2 for i in str(num)])
        

    return num == 1

num = int(input("Enter the number : "))
print(is_happy_num(num))    