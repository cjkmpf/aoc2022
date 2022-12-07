import time

start = time.time()
def entirely_contains(elf1, elf2):
    '''
    Checks to see if elf1's range entirely contains
    elf2's range
    '''
    elf1_start, elf1_end = elf1.split('-')
    elf2_start, elf2_end = elf2.split('-')

    if int(elf2_start) >= int(elf1_start):
        if int(elf2_end) <= int(elf1_end):
            return True

    return False


with open('input.txt', 'r') as f:
    pairs = f.read().split('\n')

contains_count = 0

for pair in pairs:
    elf1, elf2 = pair.split(',')

    # Check if elf1 contains elf2
    if entirely_contains(elf1, elf2):
        contains_count += 1
        continue

    # Check if elf2 contains elf1 (not sure if I can condense these into one check)
    if entirely_contains(elf2, elf1):
        contains_count += 1

end = time.time()
print(f'Found {contains_count} pairs with totally overlapping assignments.')
print(f'Calculated in {end - start}.')
