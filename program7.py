# Write a Python program to perform arithmetic calculation. This program accepts two operands and an operator then displays the calculated result.
op1 = float(input("Enter the first operand: "))
op2 = float(input("Enter the second operand: "))
operator = str(input("Enter the operator: "))
valid_operators = ['+', '-', '*', '/']
if operator not in valid_operators:
    print("Invalid operator. Please enter '+', '-', '*', or '/'.")
else:
    if operator == '+':
        result = op1 + op2
    elif operator == '-':
        result = op1 - op2
    elif operator == '*':
        result = op1 * op2
    elif operator == '/':
        if op2 != 0:  
            result = op1 / op2
        else:
            print("Error: Division by zero.")
            result = None

    if result is not None:
        print("The result of the desired operation is:",result)