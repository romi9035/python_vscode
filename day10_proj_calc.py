from calc_art import logo
import os
print(logo)


def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


oprList = {
    "+": add,
    "-": sub,
    "*": multiply,
    "/": divide}


def performCalc(firstNumber):

    if not firstNumber:
        firstNumber = float(input("What's the first number ?: "))
    for i in oprList:
        print(i)

    operation = input("Pick an operation: ")
    nextNumber = float(input("What's the next number ?: "))
    function = oprList[operation]
    if function:
        calcNumber = function(firstNumber, nextNumber)
        print(f"{firstNumber} {operation} {nextNumber} { '=' } {calcNumber}")
        return calcNumber
        # if operation == '+':
        #     calcNumber = add(firstNumber, nextNumber)
        #     print(f"{firstNumber} {operation} {nextNumber} { '=' } {calcNumber}")
        #     return calcNumber
        # elif operation == '-':
        #     calcNumber = sub(firstNumber, nextNumber)
        #     print(f"{firstNumber} {operation} {nextNumber} { '=' }  {calcNumber}")
        #     return calcNumber
        # elif operation == '*':
        #     calcNumber = multiply(firstNumber, nextNumber)
        #     print(f"{firstNumber} {operation} {nextNumber} { '=' }  {calcNumber}")
        #     return calcNumber
        # elif operation == '/':
        #     calcNumber = divide(firstNumber, nextNumber)
        #     print(f"{firstNumber} {operation} {nextNumber} { '=' }  {calcNumber}")
        #     return calcNumber
    else:
        print("Invalid operation")


flag = 'y'
calcNumber = 0
while flag == 'y' or 'n':
    calcNumber = (performCalc(calcNumber))
    flag = input(
        f"Type 'y' to continue calculating with {calcNumber}, or type 'n' to start a new calculation: ")
    if flag == 'n':
        calcNumber = 0
    os.system('cls')
