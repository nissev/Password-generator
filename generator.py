import random
import string
l = int(input("\033[92m {}\033[00m" .format("How long should the password be:")))
b = input("\033[92m {}\033[00m" .format('Can it include upper case letters? (Y/N)'))
c = input("\033[92m {}\033[00m" .format('Can it include lower case letters? (Y/N)'))
n = input("\033[92m {}\033[00m" .format('Can it include numbers? (Y/N)'))
s = input("\033[92m {}\033[00m" .format('Can it special characters? (Y/N)'))
charList = ""
r = ""

if b == 'Y':
    charList += string.ascii_uppercase
if c == 'Y':
    charList += string.ascii_lowercase
if n == 'Y':
    charList += string.digits
if s == 'Y':
    charList += string.punctuation

if l > 0 and charList != "":
    cl = len(charList)
    for i in range(l):
        r += charList[random.randint(0,cl)]
else:
    print("\033[91m {}\033[00m" .format("No password was generated! Please provide correct input."))

print(r)
