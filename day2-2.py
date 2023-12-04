filename = "day2_input.txt"
sum = 0

def find_possible_power(string):
    z = string.split(":")
    games = z[1].split(";")

    max_values = {
        "red"   : 0,
        "blue"  : 0,
        "green" : 0
    }

    for game in games:
        values = game.split(",")

        for value in values:
            _value = value.split()
            print(_value)
            if max_values[_value[1]] < int(_value[0]):
                max_values[_value[1]] = int(_value[0])

    power = 1
    for x in max_values.values():
        power *= int(x)

    return power


with open(filename) as file:
    for line in file:
        sum += find_possible_power(line)

print(sum)