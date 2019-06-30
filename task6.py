#!/usr/bin/env python

# inserted text
cipher = input()

# patterns
upattern = '0123456789ABCDEFGHIJKLMNOPQ'
lpattern = '  abcdefghigklmnopqrstuvwxyz '
l1 = []

# strings length
length = len(cipher)

# dividing without rest
dividing = length // 27

# rest from div
rest = length % 27


def converting(code, base):
    z = []
    for k in range(len(code)):
        for j in range(len(base)):
            if code[k] == base[j]:
                z.append(j)
    return z


def converting1(code, base):
    z = []
    for m in range(len(code)):
        for j in range(len(base)):
            if code[m] == j:
                z.append(base[j])
    return z


for i in range(dividing):
    l1.extend(converting(cipher[i * 27:i * 27 + 26], upattern))

l1.extend(converting(cipher[length - rest:length], upattern))

for i in range(len(l1)):
    x = l1[i] - i + 27 * (i // 27)
    if x <= 0:
        x += 27
    l1[i] = x

l1 = converting1(l1, lpattern)
for i in l1:
    print(i, end="")
