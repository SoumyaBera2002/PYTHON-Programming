def is_Prime(num):
    if(num < 2):
        return False
    elif((num==2) or (num==3)):
        return True
    else:
        is_prime = True
        i = 2
        while(i*i<=num):
            if(num % i == 0):
                is_prime = False
            else:
                is_prime = True
            i = i + 1
        if is_prime == True:
            return True
        else:
            return False
num = int(input("Enter a number : "))
res = is_Prime(num)
if res:
    print("Prime")
else:
    print("Not Prime")