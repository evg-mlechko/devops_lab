#!/usr/bin/env python
print("Insert desired lover bound")
lb = int(input())
print("Insert desired upper bound")
ub = int(input())
li = []
for i in range(lb, ub + 1):
    accepted = True
    temp = i
    while not i == 0:
        i, selfd = divmod(i, 10)
        if selfd == 0 or not temp % selfd == 0:
            accepted = False
            break
    if accepted:
        li.append(temp)
print("Self dividing numbers from scope: ")
print(li)
