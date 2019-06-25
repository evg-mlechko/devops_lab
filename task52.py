#!/usr/bin/env python
# insert any keyboard letter
print("insert any letter from keyboard ")


def letter(n):
    s = "qwertyuiopasdfghjklzxcvbnmq"
    li = s[s.find(n) + 1]
    if li == 'l':
        return True
    else:
        return False


if __name__ == "__main__":
    k = str(input())
    print(letter(k))
