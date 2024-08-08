import re

# Prompt for the file name
name = input("Enter file name: ")
if len(name) < 1:
    name = "regex_sum_2029482.txt"

# Open the file
handle = open(name)

# Initialize the sum
total_sum = 0

# Loop through each line in the file
for line in handle:
    # Find all numbers in the line
    numbers = re.findall('[0-9]+', line)
    # Convert the found numbers to integers and add to the sum
    for number in numbers:
        total_sum += int(number)

# Print the total sum
print(total_sum)