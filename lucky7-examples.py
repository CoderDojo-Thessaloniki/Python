#####################################        LUCKY 7

####################################################
print("\n\n\n       Simple  example       ")
####################################################
import random

win  = True

for i in range(3):
    luckyDigit = random.randint(1,7)
    print(luckyDigit)
    if luckyDigit != 7:
        win = False

if win == True:
    print("You have won!")
else:
    print("bad luck... next time")



####################################################
print("\n\n\n       The Maths example       ")
####################################################
import random

sum = 0

for i in range(3):
    luckyDigit = random.randint(1,7)
    print(luckyDigit)
    sum += luckyDigit

if sum == 21:
    print("You have won!")
else:
    print("bad luck... next time")



####################################################
print("\n\n\n       The String example       ")
####################################################
import random

numbers = ""

for i in range(3):
    numbers += str(random.randint(1,7))

print(numbers)

if "777" in numbers:
    print("You have won!")
else:
    print("bad luck... next time")



####################################################
print("\n\n\n\n       The Run-Until-I-Win example       ")
####################################################
import random

win = False
counter = 0

while win == False:

    win  = True
    counter += 1
    
    for i in range(3):
        luckyDigit = random.randint(1,7)
        if luckyDigit != 7:
            win = False
    

print("You have won!")
print("It took ", counter, " tries!")



####################################################
print("\n\n\n       The Run-Until-I-Win example _no-for_edition       ")
####################################################
import random

win = False
counter = 0

while win == False:

	counter += 1

	a = random.randint(1,7)
	b = random.randint(1,7)
	c = random.randint(1,7)

	if a == b == c == 7 :
		win = True


print("You have won!")
print("It took ", counter, " tries!")



####################################################
print("\n\n\n\n       The Run-Until-I-Win example _else-break_edition       ")
####################################################
import random

counter = 0

while True:

    counter += 1
    
    for i in range(3):
        luckyDigit = random.randint(1,7)
        if luckyDigit != 7:
            break
    else:
        break

print("You have won!")
print("It took ", counter, " tries!")



####################################################
print("\n\n\n\n       The Run-Until-I-Win example _ninja-hacker_edition       ")
####################################################
import random


for j in range(2**32):#Although it is not mathematically correct, the chance not to draw even once the "777" is a SUPER TINY chance with more than 1.000.001 leading zeroes!

    for i in range(3):
        if random.randint(1,7) != 7 : break
    else:
        print("You have won! \nIt took ", j, " tries!")
        break



'''
#########################################################
# This example is commented out because it is EVIL!
####################################################
print("\n\n\n\n       The Run-Until-I-Win example _recursive_edition       ")
# This is baaaaaaaaaaaad and  WILL NOT RUN  in repl.it  :P
# In case you need more recursion depth uncomment the following two lines, but have in mind that IT IS BAD practice to increase the recursion depth.
#import sys
#sys.setrecursionlimit(9999) # We need moooore recursion depth!
####################################################
import random

def luckyDraw(counter=0):
    for i in range(3):
        luckyDigit = random.randint(1,7)
        if luckyDigit != 7:
            luckyDraw(counter + 1)
        
luckyDraw()

print("You have won!")
print("It took ", counter, " tries!")
'''
