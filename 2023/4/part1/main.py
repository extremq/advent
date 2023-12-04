with open("input.txt") as f:
    lines = f.read().splitlines()

answer = 0

for line in lines:
    content = ' '.join(line.split())
    content = content.split(' ')
    content = content[2:]

    winning = []
    picked = []

    for i in range(len(content)):
        if content[i] == '|':
            winning = content[:i]
            picked = content[i+1:]
            break

    winning = {int(x) for x in winning}
    picked = {int(x) for x in picked}

    count = len(winning & picked)

    if count > 0:
        answer += 2 ** (count - 1)

print(answer)