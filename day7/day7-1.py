import time

def update_dir_totals(filesize, scoped_dirs):
    for folder in scoped_dirs:
        folder['total'] += filesize


def find_target_dirs(dir_tree):
    total = 0
    for k, v in dir_tree.items():
        if k == 'total':
            if v <= 100000:
                total += v
        else:
            total += find_target_dirs(v)

    return total

start = time.time()
with open('input.txt', 'r') as f:
    output = f.read().split('\n')

file_system = {'/': {'total': 0}}

for line in output:
    line_sections = line.split(' ')

    if line_sections[1] == 'cd':
        if line_sections[2] == '/':
            scoped_dirs = [file_system['/']]
            continue

        if line_sections[2] == '..':
            scoped_dirs.pop()
            continue

        dir_name = line_sections[2]
        current_dir = scoped_dirs[len(scoped_dirs ) - 1]
        scoped_dirs.append(current_dir[dir_name])

    elif line_sections[1] == 'ls':
        continue

    elif line_sections[0] == 'dir':
        dir_name = line_sections[1]
        current_dir = scoped_dirs[len(scoped_dirs ) - 1]
        if not current_dir.get(dir_name):
            current_dir[dir_name] = {'total': 0,}

    # I could us a RE to match for numbers for this, but I'm lazy and we know from
    # the input that the only option left is that it's a filseize number
    else: 
        filesize = int(line_sections[0])
        update_dir_totals(filesize, scoped_dirs)

total = find_target_dirs (file_system)

end = time.time()
print(file_system)
print(f'The total size of all target dirs is {total}.')
print(f'Calculated in {end - start}.')
