# Write a Python program to check whether a given year is leap year or not.
year=int(input("Enter the desired year:"))

if (year % 4 == 0 and year % 100 != 0) | (year % 400 == 0):
    print("The year",year,"is a leap year.")
else:
    print("The year",year,"is not a leap year.")