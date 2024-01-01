'''
def add_num(a,b): # it's so amazing that we don't even have to specify a return type
    return (a+b)
a = int(input("Enter a number : "))
b = int(input("Enter a number : "))
ans = add_num(a,b)
print("Ans : ",ans) ''' 

def rectangle(length,width):
    area = length * width
    parimeter = 2 * (length + width)
    return area,parimeter

length = int(input("Enter the length of a rectangle : "))
width = int(input("Enter the width of a rectangle : "))
area,parimeter = rectangle(length,width)
print("Area of the rectangle is : ",area)
print("Parimeter of the rectangle is : ",parimeter)