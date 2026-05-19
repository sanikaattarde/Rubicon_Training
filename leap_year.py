# Find leap year(only use AND operator)
year = int(input("Enter a year: "))

if year % 4 == 0:
    if year % 100 == 0 and year % 400 == 0:
        print(year, "is a leap year.")
    elif year % 100 != 0:
        print(year, "is a leap year.")
    else:
        print(year, "is not a leap year.")
else:
    print(year, "is not a leap year.")

    
# Find leap year(logical operator)
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")