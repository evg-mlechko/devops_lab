#!/usr/bin/env python
from random import randint
from collections import Counter

# n = input()
print("Insert desired length of the list: ")
li = []
for i in range(int(input())):
    li.append(randint(0, 100))
# print(numbers)
# numbers.sort(reverse=True)
element = Counter(li).most_common(1)
print('[(Most common element, ' + "number of entries)] ")
print(element)
