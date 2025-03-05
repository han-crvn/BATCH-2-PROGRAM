#Create a program that print all the odd numbers starting from 0 to 100. (Use while loop)

count = 0
num_list = []

while count < 101:

    if count % 2 != 0:
        num_list.append(count)

    count += 1

print(f"The odd numbers are {num_list}.")
