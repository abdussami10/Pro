"""
Create a program to calculate whether a year is a leap year.
"""

try:
    year = int(input("Enter a year: "))
except ValueError:
    print("Try to enter number")
except:
    print("Try agin!")

if year%400 == 0:
    print(f"{year} is leap year ")
elif year%100 == 0:
    print(f"{year} is not a leap year")
elif year%4 == 0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")