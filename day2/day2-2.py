'''
Rock = 1
Paper = 2
Scissors = 3

Lose = 0
Draw = 3
Win = 6

A = Rock
B = Paper
C = Scissors

X = Lose
Y = Draw
Z = Win
'''
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
            total_points += 1
            continue

        if opponent == 'C':
            total_points += 2
            continue

    if me == 'Y':
        if opponent == 'A':
            total_points += 4
            continue

        if opponent == 'B':
            total_points += 5
            continue

        if opponent == 'C':
            total_points += 6
            continue

    if me == 'Z':
        if opponent == 'A':
            total_points += 8
            continue

        if opponent == 'B':
            total_points += 9
            continue

        if opponent == 'C':
            total_points += 7
            continue

end = time.time()
print(f'If you follow the strategy you will earn {total_points} points.')
print(f'Calculated in {end - start}.')
