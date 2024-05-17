# Create an initial file and write the numeric array to it
initial_array = [1, 2, 3, 4, 5]

# Write the initial file
with open('initial_file.txt', 'w') as file:
    for number in initial_array:
        file.write(f"{number}\n")

# Read the initial file and double each element
doubled_numbers = []
with open('initial_file.txt', 'r') as file:
    for line in file:
        number = int(line.strip())
        doubled_numbers.append(number * 2)

# Write the doubled numbers to a new file
with open('doubled_file.txt', 'w') as file:
    for number in doubled_numbers:
        file.write(f"{number}\n")

# Calculate the sum of the doubled numbers and print it
sum_of_doubled_numbers = sum(doubled_numbers)
print("Sum of the elements:", sum_of_doubled_numbers)
