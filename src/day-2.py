from collections import Counter

doubles = 0
triples = 0

with open('day-2-input') as file:
    for line in file.readlines():
        c = Counter(line)
        for element in c.elements():
            if c[element] == 2:
                doubles += 1
                break
        for element in c.elements():
            if c[element] == 3:
                triples += 1
                break

print(doubles)
print(triples)
print(doubles*triples)

lines = []
with open('day-2-input') as file:
    lines = file.readlines()


def different_chars_indexes(x: str, y: str) -> list:
    diffs = []
    for index in range(0, len(x)):
        if x[index] != y[index]:
            diffs.append(index)

    return diffs


box_id = ""

for i in range(0, len(lines)):
    for j in range(0, len(lines)):
        if i == j:
            continue
        else:
            pos = different_chars_indexes(lines[i].strip(), lines[j].strip())
            if len(pos) == 1:
                box_id = lines[i]
                print(lines[i])
                print(lines[j])
                box_id = box_id[:pos[0]] + box_id[pos[0]+1:]
                break

print(box_id)



