#Create a program that ask user to input 2 numbers. Print "Not Equal" when the numbers are not the same.

while True:
    try:
        num1 = float(input("Enter 1st number: "))
        num2 = float(input("Enter 2nd number: "))

        if num1 != num2:
            print("Not Equal")

        else:
            print("Equal")
        break

    except ValueError:
        print("Invalid input")