import time

start = time.time()
with open('input.txt', 'r') as f:
    games = f.read().split('\n')

total_points = 0

for game in games:
    opponent, me = game.split()

    if me == 'X':
        if opponent == 'A':
            total_points += 3
            continue

        if opponent == 'B':
            continue

        if opponent == 'C':
            total_points += 6
            continue

    if me == 'Y':
        total_points += 2

        if opponent == 'A':
            total_points += 6
            continue

        if opponent == 'B':
            total_points += 3
            continue

        if opponent == 'C':
            continue

    if me == 'Z':
        total_points += 3

        if opponent == 'A':
            continue

        if opponent == 'B':
            total_points += 6
            continue

        if opponent == 'C':
            total_points += 3
            continue

end = time.time()
print(f'If you follow the strategy you will earn {total_points} points.')
print(f'Calculated in {end - start}.')
