import time

def update_dir_totals(filesize, scoped_dirs):
    for folder in scoped_dirs:
        folder['total'] += filesize


def find_del_dir(dir_tree, min_size, total=9999999999999999):
    # We don't check if total > min_size here because we *know* we are starting
    # the problem from the root of the filesystem that doesn't have enough space
    print(total)
    smallest_child = None
    for k, v in dir_tree.items():
        if k == 'total':
            continue

        child_size = v['total']

        if child_size >= min_size and child_size <= total:
            smallest_child = v
            total = child_size

    if not smallest_child:
        return total

    return find_del_dir(smallest_child, min_size, total)


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
            current_dir[dir_name] = {'total': 0}

    # I could us a RE to match for numbers for this, but I'm lazy and we know from
    # the input that the only option left is that it's a filseize number
    else: 
        filesize = int(line_sections[0])
        update_dir_totals(filesize, scoped_dirs)

file_system_size = file_system['/']['total']
free_space = 70000000 - file_system_size
min_delete_size = 30000000 - free_space
print(f'file system size is {file_system_size}.')
print(f'free space is {free_space}.')
print(f'must delete {min_delete_size}.')
delete_dir_size = find_del_dir(file_system, min_delete_size)

stop = time.time()
print(f'Smallest file that can be deleted is size {delete_dir_size}.')
print(f'Calculated in {stop - start}.')
