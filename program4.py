#Create a program that ask user to input 2 numbers. Print the quotient of the two numbers without the decimal point

while True:
    try:
        num1 = float(input("Enter 1st number: "))
        num2 = float(input("Enter 2nd number: "))

        quotient = num1 //  num2

        print(f"The quotient is {quotient:.0f}.")
        break

    except ValueError:
        print("Invalid input")