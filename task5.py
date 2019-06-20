#!/usr/bin/env python
# insert any keyboard letter
print("insert any letter from keyboard ")
n = input()
s = "qwertyuiopasdfghjklzxcvbnmq"
print("next one letter is: ")
print(s[s.find(n) + 1])
