import random
l = int(input('How long should the password be:'))
b = input('Can it include upper case letters? (Y/N)')
c = input('Can it include lower case letters? (Y/N)')
# n = input('Can it include numbers? (Y/N)')
# s = input('Can it special characters? (Y/N)')
r = ""

if l > 0:
    if b == 'Y':
        minAscii = 65
        maxAscii = 90
    if c == 'Y':
        maxAscii = 122
        print(maxAscii)
    for i in range(l):
        r += chr(random.randint(minAscii,maxAscii))

print(r)