print("Welcome to the simple Calculator")

operation = input("Enter the operation you wish to make(+|-|/|*)? ")


if operation == "+":
    number_1 = float(input("Put in your first number "))
    number_2 = float(input("Put in your second number "))
    print(f'{number_1} + {number_2} = {number_1 + number_2}')
elif operation == "-":
    number_1 = float(input("Put in your first number "))
    number_2 = float(input("Put in your second number "))
    print(f'{number_1} - {number_2} = {number_1 - number_2}')
elif operation == "/":
    number_1 = float(input("Put in your first number "))
    number_2 = float(input("Put in your second number "))
    print(f'{number_1} / {number_2} = {number_1 / number_2}')
elif operation == "*":
    number_1 = float(input("Put in your first number "))
    number_2 = float(input("Put in your second number "))
    print(f'{number_1} * {number_2} = {number_1 * number_2}')
else:
    print("Invalid operation. Please choose from +, -, /, or *.")