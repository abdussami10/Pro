"""
Create a program to calculate a score. If someone's score is below 33, print You failed! otherwise print You passed!
"""

try:
    score = int(input("Enter your exam score: "))
except ValueError:
    print("Try to enter number")
except:
    print("Try agin")

if score >= 33 and score <= 100:
    print("You passed!")
elif score >= 0 and score <= 32:
    print("You failed!")
else:
    print("You enter something wrong ")