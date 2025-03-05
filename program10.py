#Create a program that ask user to input 2 numbers. Print all the numbers between the two numbers.

nums = []

while True:
    num1 = int(input("Enter 1st number: "))
    num2 = int(input("Enter 2nd number: "))

    if abs(num1 - num2) > 1:
        if num1 < num2:
            for i in range(num1 + 1, num2):
                if i not in nums:
                    nums.append(i)
        else:
            for i in range(num2 + 1, num1):
                if i not in nums:
                    nums.append(i)
       
        print(f"The number between {num1} and {num2}: {nums}")
        break
    
    else:
        print(f"There is no number between {num1} and {num2}.")
        break