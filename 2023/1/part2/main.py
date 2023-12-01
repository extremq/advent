with open("input.txt") as f:
    lines = f.read().splitlines()

total_sum = 0


def check_for_digit_spelt(string):
    digit_map = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }

    for digit in digit_map:
        if string.startswith(digit):
            return digit_map[digit]

    return None

for line in lines:
    first = None
    second = None

    for index, character in enumerate(line):
        if character.isdigit():
            first = int(character)
            break
        elif first := check_for_digit_spelt(line[index:]):
            break

    for index, character in enumerate(line[::-1]):
        if character.isdigit():
            second = int(character)
            break
        elif second := check_for_digit_spelt(line[len(line) - 1 - index:]):
            break

    total_sum += first * 10 + second

print(total_sum)
