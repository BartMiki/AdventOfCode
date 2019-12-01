from math import floor

def calculate(value):
    return floor(value / 3.0) - 2

def calculate_with_fuel(value):
    result = floor(value / 3.0) - 2
    if result <= 0:
        return 0
    else:
        return result + calculate_with_fuel(result)

values_part_1 = None
values_part_2 = None
with open('../data/day_01.txt') as data:
    values = list(map(lambda raw: int(raw.strip()), data.readlines()))
    values_part_1 = map(calculate, values)
    values_part_2 = map(calculate_with_fuel, values)

# part 1
print(sum(values_part_1))
print(sum(values_part_2))
# part 2

print(calculate_with_fuel(1969))