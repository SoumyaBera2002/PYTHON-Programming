def odd_even(num):
    if(num % 2 == 0):
        return True
    else:
        return False

num = int(input("Enter a number : "))
res = odd_even(num)
if res:
    print("The number is even ")
else:
    print("The number is odd ")
