
def calculator():
    while True:
        try:
            firstNumber = float(input("Enter the first number here: "))
            break
        except ValueError:
            print("Invalid input. Please input a valid number.")
    while True:
        try :
            secondNumber = float(input("Enter the second number here: "))
            break
        except ValueError:
            print("Invalid input. Please input a valid number.")
    operation = input("Enter the operation you want to perform (+, -, *, /): ")

    if operation == "+":
        result =  firstNumber + secondNumber
        print(f"The result of the sum is : {result}")
    elif operation == "-":
        result =  firstNumber - secondNumber
        print(f"The result of the difference is : {result}")
    elif operation == "*":
        result =  firstNumber * secondNumber
        print(f"The result of the product is : {result}")
    elif operation == "/":
        if secondNumber == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result =  firstNumber / secondNumber
            print(f"The result of the quotient is : {result}")
    else:
        print("The operation you entered is not valid")

calculator()
