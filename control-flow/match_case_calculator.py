first_number = int (input("Enter the first number:"))
second_number = int (input("Enter the second number:"))
operation = str(input("Choose the operation (+, -, *, /):."))
if operation == "+":
    result = first_number + second_number
elif operation == "-":
    result = first_number - second_number
elif operation == "*":
    result = first_number * second_number
else:
    if first_number < 0  or second_number < 0:
        print("Cannot divide by zero.")
    else:
        result = first_number / second_number
print("The result is ",result)