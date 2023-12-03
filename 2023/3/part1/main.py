with open("input.txt") as f:
    lines = f.read().splitlines()

matrix = []
answer = 0


def check_for_symbol(row, column):
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

        if matrix[new_row][new_column] != "." and not matrix[new_row][new_column].isdigit():
            return True

    return False


for line in lines:
    matrix.append(list(line))

for row in range(len(matrix)):
    cum_number = 0
    found_symbol = False
    for column in range(len(matrix[row])):
        if matrix[row][column].isdigit():
            cum_number = cum_number * 10 + int(matrix[row][column])
            if check_for_symbol(row, column):
                found_symbol = True
        else:
            if found_symbol:
                answer += cum_number

            cum_number = 0
            found_symbol = False

    if found_symbol:
        answer += cum_number

print(answer)
