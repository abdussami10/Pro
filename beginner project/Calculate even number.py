"""
Create a program to calculate whether a number is even or odd.
"""

try:

    num = int(input("Enter a number: "))
except ValueError:
    print("Try to input number")
except:
    print("Try agin!")

if num%2 == 0:
    print(num ," is even Number")

else:
    print(num, " is not even Number")
    print("This is odd Number!")