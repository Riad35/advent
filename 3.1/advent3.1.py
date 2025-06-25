import re

def sum_enabled_mul(filename):
    with open(filename, 'r') as file:
        corrupted_memory = file.read()

    # Patterns to match valid instructions
    mul_pattern = re.compile(r'mul\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*\)')
    do_pattern = re.compile(r'do\(\)')
    dont_pattern = re.compile(r"don't\(\)")

    mul_enabled = True
    total = 0

    # We'll scan the string left to right, finding all do, don't, and mul instructions in order
    # For this, we can find all matches of these three patterns combined with their positions
    combined_pattern = re.compile(r"mul\(\s*\d{1,3}\s*,\s*\d{1,3}\s*\)|do\(\)|don't\(\)")

    for match in combined_pattern.finditer(corrupted_memory):
        instr = match.group()

        if do_pattern.fullmatch(instr):
            mul_enabled = True
        elif dont_pattern.fullmatch(instr):
            mul_enabled = False
        else:
            # It's a mul instruction
            if mul_enabled:
                # Extract the two numbers from mul()
                nums = mul_pattern.fullmatch(instr)
                if nums:
                    a, b = int(nums.group(1)), int(nums.group(2))
                    total += a * b

    return total

# Example usage:
# print(sum_enabled_mul("corrupted_memory.txt"))
