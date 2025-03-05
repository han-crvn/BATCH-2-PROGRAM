#Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero or ending five.

num_list = []

for num in range(101):
    if not str(num).endswith("0") and not str(num).endswith("5"):
        num_list.append(num)

print(f"The numbers are {num_list}.")