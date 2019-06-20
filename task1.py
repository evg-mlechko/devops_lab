#!/usr/bin/env python
print("Insert x, y, z respectively:")
x, y, z = int(input()), int(input()), int(input())
print("Insert parameter N:")
N = int(input())
print("Lists of all possible coordinates  by task: \n")
print([[a, b, c]
       for a in range(0, x + 1)
       for b in range(0, y + 1)
       for c in range(0, z + 1)
       if a + b + c != N])
