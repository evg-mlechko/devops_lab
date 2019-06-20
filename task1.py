#!/usr/bin/env python

x, y, z, N = int(input()), int(input()), int(input()), int(input())
print([[a, b, c]
       for a in range(0, x + 1)
       for b in range(0, y + 1)
       for c in range(0, z + 1)
       if a + b + c != N])
