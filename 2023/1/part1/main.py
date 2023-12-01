with open("input.txt") as f:
    lines = f.read().splitlines()

total_sum = 0

for line in lines:
    first = None
    second = None

    for character in line:
        if character.isdigit():
            first = int(character)
            break

    for character in line[::-1]:
        if character.isdigit():
            second = int(character)
            break

    total_sum += first * 10 + second

print(total_sum)