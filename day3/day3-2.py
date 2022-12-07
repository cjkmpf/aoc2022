import time

start = time.time()
def get_priority_value(letter):
    if letter.islower():
        # Assigns a-z value of 1-26
        return ord(letter) - 96

    # Assigns A-Z value of 27-52
    return ord(letter) - 38


with open('input.txt', 'r') as f:
    rucksacks = f.read().split('\n')

total_priority = 0

for n in range(0, len(rucksacks), 3):
    rucksack1 = rucksacks[n]
    rucksack2 = rucksacks[n+1]
    rucksack3 = rucksacks[n+2]

    for item in rucksack1:
        if item in rucksack2:
            if item in rucksack3:
                total_priority += get_priority_value(item)
                break

end = time.time()
print(f'Group items have a total priority of {total_priority}.')
print(f'Calculated in {end - start}.')
