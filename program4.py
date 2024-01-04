# Write a Python program to compute simple interest for given Principal amount, time and rate of interest.
principal_amount=float(input("Enter the amount:"))
time=float(input("Enter the time:"))
rate_of_interest=float(input("Enter the rate of interest:"))

simple_interest=(principal_amount*rate_of_interest*time)/100
print("The simple interest of the principal amount ₹",principal_amount,",rate of interest",rate_of_interest,"% , time",time,"is :",simple_interest)