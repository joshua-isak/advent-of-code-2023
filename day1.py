# Find the first and last digit in each line and put them together to form a two digit number, return sum of all lines

filename = "day1_input.txt"
sum = 0



def find_number(string):
    digits = []

    # Find all digits in string
    for x in string:
        if x.isdigit():
            digits.append(x)

    # Return number generated from first and last digits
    return int(digits[0]) * 10 + int(digits[-1])



# Read each line and call find_number
# Add the number to the sum
with open(filename) as file:
    for line in file:
        sum += find_number(line)


# Print result!
print(sum)