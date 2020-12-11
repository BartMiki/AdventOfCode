with open('data/day_1.txt') as file:
    data = [int(line.strip()) for line in file.readlines()]

differences = set()
for number in data:
    if number in differences:
        print(number * (2020-number))
        break
    else:
        differences.add(2020-number)


differences = {2020-n: n for n in data}
two_differences = {}
for key, value in differences.items():
    for n in data:
        if (key - n) >= 0:
            two_differences[key - n] = value*n

for number in data:
    if number in two_differences:
        print(number * two_differences[number])
        break