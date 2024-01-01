length = int(input("Enter the length of the dictonary : "))
user_dict = {}

for i in range(length):
    key = input("Enter the key : ")
    value = input("Enter the value : ")
    user_dict[key] = value
    
print("The user defined Dictonary is : \n",user_dict)