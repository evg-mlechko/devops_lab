#!/usr/bin/env python

print("insert required data ")
li = {}
for i in range(int(input())):
    x = input()
    if x not in li:
        li[x] = 1
    else:
        li[x] = li[x] + 1
print("line one: quantity unique words\nline two: quantity appearance each of the word")
print(len(li))
for i in li:
    print(li[i], end=" ")
