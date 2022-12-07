import re

start = time.time()
crates = {
    '1': ['T', 'D', 'W', 'Z', 'V', 'P'],
    '2': ['L', 'S', 'W', 'V', 'F', 'J', 'D'],
    '3': ['Z', 'M', 'L', 'S', 'V', 'T', 'B', 'H'],
    '4': ['R', 'S', 'J'],
    '5': ['C', 'Z', 'B', 'G', 'F', 'M', 'L', 'W'],
    '6': ['Q', 'W', 'V', 'H', 'Z', 'R', 'G', 'B'],
    '7': ['V', 'J', 'P', 'C', 'B', 'D', 'N'],
    '8': ['P', 'T', 'B', 'Q'],
    '9': ['H', 'G', 'Z', 'R', 'C'] 
}

with open('input.txt', 'r') as f:
    actions = f.read().split('\n')

action_pattern = re.compile('move ([0-9]+) from ([0-9]) to ([0-9])')

for action in actions:
    action_match = re.match(action_pattern, action)

    move_count, from_stack, to_stack = action_match.groups()
    move_count = int(move_count)

    for n in range(move_count):
        crates[to_stack].append(crates[from_stack].pop())

final_tops = ''

for k, v in crates.items():
    final_tops += v[len(v) - 1]

end = time.time()
print(f'The top of each stack is {final_tops}.')
print(f'Calculated in {end - start}.')
