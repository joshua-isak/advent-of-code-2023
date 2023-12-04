# Find the first and last digit in each line (can be expressed as string!) and put them together to form a two digit number
# return sum of all lines

filename = "day1_input.txt"
sum = 0
iter = 1

numbers = {
    "one"   : 1,
    "two"   : 2,
    "three" : 3,
    "four"  : 4,
    "five"  : 5,
    "six"   : 6,
    "seven" : 7,
    "eight" : 8,
    "nine"  : 9
}

def find_real_number(string):
    number_locations = {}

    # Find all digits in string and record their locations
    for x in range(len(string)):
        if string[x].isdigit():
            number_locations[x] = int(string[x])

    # Find all spelled numbers in string and record their locations
    for num in numbers:
        start_index = 0                                     # gotta make sure we search the entire string
        while True:
            location = string.find(num, start_index)
            if location == -1: break                        # not found, carry on, close da loop
            number_locations[location] = numbers[num]
            start_index += len(num)

    # Find first and last locations
    print(iter)
    print(number_locations)
    max_loc = max(number_locations.keys())
    min_loc = min(number_locations.keys())

    # Return number generated from first and last locations
    number = number_locations[min_loc] * 10 + number_locations[max_loc]
    print("result: " + str(number))
    return number




# Read each line and call find_number
# Add the number to the sum
with open(filename) as file:
    for line in file:
        sum += find_real_number(line)
        iter += 1


# Print result!
print(sum)