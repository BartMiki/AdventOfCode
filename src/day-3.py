import re
from collections import Counter

r = re.compile('^#\d+ @ (\d+),(\d+): (\d+)x(\d+)*$')


def get_cords(x: int, y: int, x_span: int, y_span: int) -> list:
    out_list = []

    for i in range(x, x + x_span):
        for j in range(y, y + y_span):
            out_list.append('{} {}'.format(i, j))

    return out_list


c_list = []

with open('data/day-3-input') as file:
    for line in file.readlines():
        result = r.match(line)
        c_list.extend(get_cords(int(result.group(1)), int(result.group(2)), int(result.group(3)), int(result.group(4))))

c = Counter()
for elem in c_list:
    c[elem] += 1

claims = 0
for pair in set(c.elements()):
    if c[pair] > 1:
        claims += 1

print(claims)