#Create a program that ask user to input 10 numbers. Print the result of the first number minus all of the remaining numbers.

total = 0

for i in range(10):
    while True:
        try:
            num = float(input(f"[{i + 1}] Enter the number: "))

            if i == 0:
                total += num
            
            else:
                total -= num

            break

        except ValueError:
            print("Invalid input.")

print(f"The result is {total}.")