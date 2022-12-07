import time

start = time.time()
with open('input.txt', 'r') as f:
    all_calories = f.read()

elves = all_calories.split('\n\n')

first = 0
second = 0
third = 0


for elf in elves:
    calorie_count = 0
    calories = elf.split('\n')

    for calorie in calories:
        calorie_count += int(calorie)

    if calorie_count > first:
        third = second
        second = first
        first = calorie_count
        continue

    if calorie_count > second:
        third = second
        second = calorie_count
        continue

    if calorie_count > third:
        third = calorie_count

total_calories = first + second + third

end = time.time()
print(f'The top three elves are carrying {total_calories} calories.')
print(f'Calculated in {end - start}.')
