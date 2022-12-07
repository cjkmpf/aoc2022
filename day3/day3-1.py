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

for sack in rucksacks:
    compartment1 = sack[:int(len(sack)/2)]
    compartment2 = sack[int(len(sack)/2):len(sack)]

    for item in compartment1:
        if item in compartment2:
            total_priority += get_priority_value(item)

            break

end = time.time()
print(f'Misplaced items have a total priority of {total_priority}.')
print(f'Calculated in {end - start}.')
