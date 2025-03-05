#Create a program that ask user to input 2 numbers. Print the smaller number.

while True:
    try:
        num1 = float(input("Enter 1st number: "))
        num2 = float(input("Enter 2nd number: "))

        if num1 < num2:
            print(f"{num1} is the smaller number.")
        
        elif num2 < num1:
            print(f"{num2} is the smaller number.")
        
        else:
            print("Both are equal.")
        break

    except ValueError:
        print("Invalid input")