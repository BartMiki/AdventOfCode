import re
from typing import List

minute_match = re.compile(r'^.*:(\d+)')
id_match = re.compile(r'^.*#(\d+)')


def extract_minute(line: str) -> int:
    result = minute_match.match(line).group(1)
    return int(result)


def extract_id(line: str) -> int:
    result = id_match.match(line).group(1)
    return int(result)


lines = []
guard_sleeptime = {}

with open('data/day-4-input') as file:
    for line in file.readlines():
        lines.append(line.strip())

lines.sort()

i = 0
current_guard_id = None
while i < len(lines):
    line = lines[i]
    if '#' in line:
        current_guard_id = extract_id(line)
        if current_guard_id not in guard_sleeptime.keys():
            guard_sleeptime[current_guard_id] = 0
        i += 1
    else:
        start = extract_minute(lines[i])
        i +=1 
        end = extract_minute(lines[i])
        i += 1
        guard_sleeptime[current_guard_id] += (end - start)

sleepiest_guard = max(zip(guard_sleeptime.values(), guard_sleeptime.keys()))
print(sleepiest_guard)

sleepiest_guard_id = sleepiest_guard[1]

def individual_minutes(start_minute: int, stop_minute: int , total_minutes: List[int]) -> List[int]:
    for minute in range(start_minute, stop_minute):
        total_minutes[minute] += 1

    return total_minutes


minutes = [0 for x in range(0, 60)]
i = 0
while i < len(lines):
    line = lines[i]
    if '#' in line:
        current_guard_id = extract_id(line)
        i += 1
    else:
        start = extract_minute(lines[i])
        i +=1 
        end = extract_minute(lines[i])
        i += 1
        if current_guard_id == sleepiest_guard_id:
            individual_minutes(start, end, minutes)

most_slept_minute = minutes.index(max(minutes))
print(sleepiest_guard_id * most_slept_minute)