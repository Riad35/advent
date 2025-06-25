import re

# Replace 'input.txt' with the path to your file containing the corrupted memory
with open('math.txt', 'r') as file:
    corrupted_memory = file.read()

pattern = r'mul\((\d{1,3}),(\d{1,3})\)'

matches = re.findall(pattern, corrupted_memory)

total = 0
for x, y in matches:
    total += int(x) * int(y)

print(total)
