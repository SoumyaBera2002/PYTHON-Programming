def leap_year(year):
    if (year % 4 == 0):
        if ((year % 100 == 0) and (year % 400 == 0)):
            return True
        elif (year % 100 != 0):  # Added this condition for clarity
            return True
        else:
            return False
    else:
        return False

year = int(input("Enter a year: "))  # Convert input to integer
res = leap_year(year)
if res:
    print("The year is a leap year")
else:
    print("The year is not a leap year")
    