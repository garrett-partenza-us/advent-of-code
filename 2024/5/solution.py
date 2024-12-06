from functools import partial
from functools import cmp_to_key


def is_valid_update(nums, rules):

    for idx, num in enumerate(nums):

        after = nums[idx+1:]

        if num in rules:

            for before in rules[num]:

                if before in after:

                    return False

    return True

def custom_order(l, r, rules=None):

    if rules[l] and r in rules[l]:
        return 1

    elif rules[r] and l in rules[r]:
        return -1

    else:
        return 0



with open("input.txt", 'r') as f:

    rules = {} # For each number, list numbers which must come prior

    for line in f:

        if line.strip():
            
            first, second = line.strip().split("|")

            if second not in rules.keys():

                rules[second] = []

            rules[second].append(first)

        else:

            break

    sum = 0

    invalid_updates = []

    for line in f:

        nums = list(map(str, line.strip().split(",")))

        if is_valid_update(nums, rules):

            middle = len(nums) // 2

            sum += int(nums[middle])

        else:

            invalid_updates.append(nums)

    print(sum)

    sum = 0

    custom_order_wrapper = partial(custom_order, rules=rules)

    for nums in invalid_updates:

        nums = sorted(nums, key=cmp_to_key(custom_order_wrapper))

        middle = len(nums) // 2
        
        sum += int(nums[middle])

    print(sum)
