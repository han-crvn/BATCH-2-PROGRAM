#Create a program that ask user to input 10 numbers. Print how many are even numbers.

num_list =[]

for i in range(10):
    while True:
        try:
            num = float(input(f"[{i + 1}] Enter the number: "))

            if num % 2 == 0:
                num_list.append(num)

            break
    
        except ValueError:
            print("Invalid input.")

print(f"The total even numbers in the list is {len(num_list)}.")