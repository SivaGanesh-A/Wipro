from calendar import *
year = int(input("Enter a year number: "))
# Month = int(input("Enter a month number: "))


# str = month(year, Month)
# print(str)

if isleap(year):
    print(year, "is leap year")
else:
    print(year, "is not a leap year")
    