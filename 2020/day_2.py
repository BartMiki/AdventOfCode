import re
from collections import namedtuple, Counter

pattern = re.compile(r'(?P<lower>\d+)-(?P<upper>\d+) (?P<character>\w): (?P<password>\w+)')
Password = namedtuple('Password', ['lower', 'upper', 'character', 'password'])

def parse_line(line):
    match = pattern.match(line.strip())
    return Password(int(match['lower']), int(match['upper']), match['character'], match['password'])


with open('data/day_2.txt') as file:
    data = [parse_line(line) for line in file.readlines()]


valid_passwords = 0
for password in data:
    count = Counter(password.password).get(password.character, 0)
    if password.lower <= count <= password.upper:
        valid_passwords += 1

print(valid_passwords)

valid_passwords = 0
for password in data:
    pair = (password.password[password.lower-1], password.password[password.upper-1])
    if pair[0] != pair[1] and password.character in pair:
        valid_passwords += 1

print(valid_passwords)