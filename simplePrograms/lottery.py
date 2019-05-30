#Made by Cliff Jorgensen

#this program will generate 2 random 5 digit lottery numbers

import random

number1 = [0,0,0,0,0]
number2 = []

#generates random number and indexes value to list number1

value = random.randint(0,9)
number1[0] = value
value = random.randint(0,9)
number1[1] = value
value = random.randint(0,9)
number1[2] = value
value = random.randint(0,9)
number1[3] = value
value = random.randint(0,9)
number1[4] = value

#generates random number and appends value to empty list number2

value = random.randint(0,9)
number2.append(value)
value = random.randint(0,9)
number2.append(value)
value = random.randint(0,9)
number2.append(value)
value = random.randint(0,9)
number2.append(value)
value = random.randint(0,9)
number2.append(value)

print ("number 1 ", number1)
print()
print ("number 2 ", number2)

