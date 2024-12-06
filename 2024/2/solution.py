# Part One
import numpy as np

sum = 0

with open("input.txt", "r") as f:

    for line in f:

        nums = list(map(int, line.split()))

        is_less = lambda x, y: x < y
        is_greater = lambda x, y: x > y
        is_small_step = lambda x, y: abs(x-y)<=3

        first, second = nums[0], nums[1]

        if first < second:
            op = is_less
        elif first > second:
            op = is_greater
        else:
            continue

        is_safe = True
        leeway = 1

        for idx in range(len(nums)-1):

            if not op(nums[idx], nums[idx+1]) or not is_small_step(nums[idx], nums[idx+1]):

                if not leeway:

                    is_safe = False
                    break
                
                else:

                    leeway -= 1

        if is_safe:

            sum+=1

print(sum)
