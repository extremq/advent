import re

with open("input.txt") as f:
    lines = f.read().splitlines()

total_sum = 0

rules_map = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

for line in lines:
    details = re.match(r"Game (\d+):(.*)", line)
    number = int(details.group(1))
    rounds = details.group(2).strip().split("; ")

    possible = True

    for round in rounds:
        picks = round.split(", ")
        for pick in picks:
            amount, color = pick.split(" ")

            amount = int(amount)
            if rules_map[color] < amount:
                possible = False

    if possible:
        total_sum += number

print(total_sum)