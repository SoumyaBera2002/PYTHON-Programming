def factorial(num):
    if((num==0) or (num==1)):
        return 1
    return num*factorial(num-1)
num = int(input("Enter a number : "))
res = factorial(num)
print("The factorial of the number is : "+str(res))