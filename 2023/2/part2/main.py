import re

with open("input.txt") as f:
    lines = f.read().splitlines()

total_sum = 0

for line in lines:
    details = re.match(r"Game (\d+):(.*)", line)
    number = int(details.group(1))
    rounds = details.group(2).strip().split("; ")

    maximums = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }

    for round in rounds:
        picks = round.split(", ")
        for pick in picks:
            amount, color = pick.split(" ")
            amount = int(amount)

            maximums[color] = max(maximums[color], amount)

    power = maximums["red"] * maximums["green"] * maximums["blue"]
    total_sum += power

print(total_sum)