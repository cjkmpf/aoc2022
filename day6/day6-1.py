import time

start = time.time()
with open('input.txt', 'r') as f:
    data_stream = f.read()

char_buffer = []
for n in range(len(data_stream)):
    current_char = data_stream[n]

    while current_char in char_buffer:
        char_buffer.pop(0)

    char_buffer.append(current_char)

    if len(char_buffer) == 4:
        end = time.time()
        print(f'Found start of packet marker at position {n + 1}')
        print(f'Calculated in {end - start}.')
        break
