# Write a Python program to accept length and width of a rectangle and compute its perimeter and area.
length=float(input("Enter the length of rectangle:"))
width=float(input("Enter the width of rectangle:"))

area=length * width
print("The area of rectangle of length",length,"and width",width,"is :",area)
perimeter=2*(length+width)
print("The perimeter of rectangle of length",length,"and width",width,"is :",perimeter)