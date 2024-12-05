from collections import Counter
import numpy as np


# Part One
list1, list2 = [], []

with open("input.txt", 'r') as f:
    
    for line in f:
        num1, num2 = tuple((map(int, line.split())))
        list1.append(num1)
        list2.append(num2)

    list1.sort()
    list2.sort()
    list1, list2 = np.array(list1), np.array(list2)
    sum = np.sum(np.absolute(list1 - list2))

print(sum)

#Part Two
list1, list2 = [], []

with open("input.txt", 'r') as f:
    
    for line in f:
        num1, num2 = tuple((map(int, line.split())))
        list1.append(num1)
        list2.append(num2)

    lookup = dict(Counter(list2))

    sum = 0
    for num in list1:
        weight = lookup.get(num)
        if not weight:
            weight = 0
        sum += weight * num

print(sum)



    
