import re

ENABLED = True

def scan_muls(s: str):
    global ENABLED
    pattern = r"(.*?)(mul\(\d+(?:,\d+)\))"
    enabled_pattern = r"do\(\)|don't\(\)"
    sum = 0
    matches = re.findall(pattern, s)
    for before, match in matches:
        args = re.search("\d+(?:,\d+)", match)
        enabled_flags = re.findall(enabled_pattern, before)
        if enabled_flags:
            flag = enabled_flags[-1]
            if flag == "do()":
                ENABLED = True
            else:
                ENABLED = False
        if ENABLED:
            factors =list(map(int, args.group(0).split(",")))
            print(enabled_flags, factors)
            sum += factors[0] * factors[1]
    return sum

sum = 0

with open("input.txt", 'r') as f:

    for line in f:

        sum += scan_muls(line)

print(sum)



