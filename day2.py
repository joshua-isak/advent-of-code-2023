filename = "day2_input.txt"
sum = 0

# Max Values of blocks
max_vals = {
    "red"   : 12,
    "blue"  : 14,
    "green" : 13
}


def find_possible(string):
    z = string.split(":")
    game_num = z[0][5:]
    games = z[1].split(";")

    for game in games:
        values = game.split(",")

        for value in values:
            _value = value.split()
            print(_value)
            if max_vals[_value[1]] < int(_value[0]):
                return 0        # i want to break free

    return int(game_num)



with open(filename) as file:
    for line in file:
        sum += find_possible(line)

print(sum)