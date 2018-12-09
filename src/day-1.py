total_sum = 0

with open('day-1-input') as file:
    for line in file.readlines():
        total_sum += int(line)

# Part 1
print(total_sum)

total_sum = 0
all_frequencies = []
first_repeat = 0
encountered_so_far = {0}

with open('day-1-input') as file:
    for line in file.readlines():
        all_frequencies.append(int(line))

i = 0
while True:
    total_sum += all_frequencies[i]
    if total_sum in encountered_so_far:
        first_repeat = total_sum
        break
    else:
        encountered_so_far.add(total_sum)

    i += 1
    i %= len(all_frequencies)

# Part 2
print(first_repeat)

