import time

start = time.time()
def any_overlap(elf1, elf2):
    '''
    Checks to see if elf1's range entirely contains
    elf2's range
    '''
    elf1_start, elf1_end = elf1.split('-')
    elf2_start, elf2_end = elf2.split('-')

    elf1_start = int(elf1_start)
    elf1_end = int(elf1_end)
    elf2_start = int(elf2_start)
    elf2_end = int(elf2_end)

    # Elf 2 contains Elf 1
    if (elf1_start >= elf2_start) and (elf1_end <= elf2_end):
        return True

    # Elf 1 contains Elf 2
    if elf2_start >= elf1_start and elf2_end <= elf1_end:
        return True

    # Any overlap
    if elf1_start >= elf2_start and elf1_start <= elf2_end:
        return True

    if elf2_start >= elf1_start and elf2_start <= elf1_end:
        return True

    return False


with open('input.txt', 'r') as f:
    pairs = f.read().split('\n')

contains_count = 0

for pair in pairs:
    elf1, elf2 = pair.split(',')

    # Check if elf1 contains elf2
    if any_overlap(elf1, elf2):
        contains_count += 1
        continue

end = time.time()
print(f'Found {contains_count} pairs with overlapping assignments.')
print(f'Calculated in {end - start}.')