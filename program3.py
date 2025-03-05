#Create a program that ask user to input 2 numbers. Print the difference of the two numbers.

while True:
    try:
        num1 = float(input("Enter 1st number: "))
        num2 = float(input("Enter 2nd number: "))

        difference = num1 - num2

        print(f"The difference is {difference}.")
        break

    except ValueError:
        print("Invalid input")