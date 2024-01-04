# Write a Python program to print table of a given number.
number=int(input("Enter the number for multiplication table:"))
n=int(input("Enter the number for range:"))
i=1

print("The multiplication table for",number,"is :")
for i in range(1,n+1):
    multiply=number*i
    print(number,"x",i,"=",multiply)