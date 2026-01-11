def FizzBuzz(num):
    counter1 , counter2  =  0 , 0
    for i in range(1,num + 1):
        counter1 += 1
        counter2 += 1
        if counter1 == 3:
            counter1 = 0
            print("Fizz")
            continue
        if counter2 == 5:
            counter2 = 0
            print("Buzz")
            continue  
        print(i)  
    return "Done"
num = int(input("Enter the number : "))
print(FizzBuzz(num))
