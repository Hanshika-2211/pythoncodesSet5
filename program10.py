# Write a Python Program to print first n Natural numbers and their sum.
natural_n=int(input("Enter the term:"))
sum=0

print("The sum of natural numbers upto",natural_n,"is :")
for i in range(1,natural_n+1):
    sum += i
print(sum)