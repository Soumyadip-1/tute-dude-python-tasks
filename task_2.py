# Task 2: Create a Personalized Greeting
# Problem Statement: Write a Python program that:
# 1.  Takes a user's first name and last name as input.
# 2.  Concatenates the first name and last name into a full name.
# 3.  Prints a personalized greeting message using the full name.


fn = input("Enter your first name : ")
ln = input("Enter your last name : ")

fullName = fn+" "+ln
print("Hello,",fullName+"! Welcome to python program.")