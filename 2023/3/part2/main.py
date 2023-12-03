with open("input.txt") as f:
    lines = f.read().splitlines()

matrix = []
answer = 0

gears = {}
count = {}

def check_for_gear(row, column):
    directions = [
        (0, 1),
        (1, 0),
        (1, 1),
        (-1, 1),
        (1, -1),
        (-1, -1),
        (-1, 0),
        (0, -1),
    ]

    for direction in directions:
        new_row = row + direction[0]
        new_column = column + direction[1]

        if new_row < 0 or new_row >= len(matrix):
            continue
        if new_column < 0 or new_column >= len(matrix[new_row]):
            continue

        if matrix[new_row][new_column] == "*":
            return new_row, new_column

    return None


for line in lines:
    matrix.append(list(line))

for row in range(len(matrix)):
    cum_number = 0
    gear_position = None
    for column in range(len(matrix[row])):
        if matrix[row][column].isdigit():
            cum_number = cum_number * 10 + int(matrix[row][column])
            if not gear_position:
                gear_position = check_for_gear(row, column)
        else:
            if gear_position:
                if gear_position in gears:
                    gears[gear_position] *= cum_number
                    count[gear_position] += 1
                else:
                    gears[gear_position] = cum_number
                    count[gear_position] = 1

            gear_position = None
            cum_number = 0
    if gear_position:
        if gear_position in gears:
            gears[gear_position] *= cum_number
            count[gear_position] += 1
        else:
            gears[gear_position] = cum_number
            count[gear_position] = 1

for gear_position in gears:
    if count[gear_position] == 2:
        answer += gears[gear_position]

print(answer)
