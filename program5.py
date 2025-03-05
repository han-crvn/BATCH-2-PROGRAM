#Create a program that ask user to input 2 numbers. Print the remainder when the first number is divided by the second number.

while True:
    try:
        num1 = float(input("Enter 1st number: "))
        num2 = float(input("Enter 2nd number: "))

        remainder = num1 %  num2

        print(f"The remainder is {remainder}")

    except ValueError:
        print("Invalid input")

    except ZeroDivisionError:
        print("Number can not be divided by zero")