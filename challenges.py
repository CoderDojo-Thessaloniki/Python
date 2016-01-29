from statistics import mean
import random
##########################################################





#1#########################################################
# Print your age!  Hint: fix the line of code below
print(100)

#2#########################################################
# Print messages "Hello, World!" and "Hello CoderDojo class!" Hint: use two separate print() commands
print(" :) ")

#3#########################################################
# Print your own message using tab and newline characters  Hint: /t and /n and fix the line of code below
print("I 'm a ninja!")

#4#########################################################
# Write a list with some animals and then print them within a loop  Hint: for i in list  and fix the list!
animals = ["mouse","keyboard","dvd"]

#5#########################################################
# Ask user for his/her name and print a "Welcome name" message Hint: fix the two lines of code below
msg = input("question?")
print("welcome!")

#6#########################################################
# Is it true that  a*0==c*o , d == 5/10 , o*c == [] , o/7 <= a , a*b*c*o == d-1/10 , d/10 != 65025/255**2/100 ?    
b = 5
o = 0
a = o
c = ()
d = 0.1

#7#########################################################
# Write a loop to print the numbers between 41 and 67 (inclusive) Hint: range(start,end+1) and fix the function below
for num in range(22):
    print(6)

#8#########################################################
# From the list below print only every second letter  Hint: letters[start:stop:step]  and fix the print() below
letters = ["a", "b", "c", "a", "b", "c", "a", "b", "c", "a", "b", "c", "a", "b", "c", "a", "b", "c", "z"]
print(letters[::])

#9#########################################################
# Print the alphabet backwards  Hint: negative step
alphabet = "abcdefghijklmnopqrstuvwxyz"
print(alphabet[::])

#10#########################################################
# Find the missing letters from the alphabet from the ssttrr  Hint: for letter in alphabet, if letter not in ssttrr
ssttrr = "abcdefghjklmopqrtuwxyz"

#11#########################################################
# Calculate the square of a number using a function  Hint: def square_function(): and the power symbol is **
asq = 9

#12#########################################################
# Can you print() a square shape?  Hint: use "|" and "_" and fix the loop
print("up")
for i in range(1):
    print("left side space right side")
print("bottom")
    
#13#########################################################
# Check if there is any number in the text  Hint: use char.isdigit() where "char in text"
text = "This is a text te11ing you it is a text!"

#14#########################################################
# Find the Best and Worst Scores  Hint: use min(...) and max(...)
game_scores = [100,22,233,5,456,0,2,101]

#15#########################################################
# Find the average height   Hint: use sum(...) and len(...)
ninjas_height = [180,160,120,170,169,145,133]

#16#########################################################
# Create a Maths function calculator for the f(x)=x^2+7x+5  Hint: like the example below
def f(x):
    return x**4 + 2*x - 1

#17#########################################################
# Create a Rectangular Area Calculator  Hint: Follow the example of the Square
class Square():
    pass

Square.side1 = Square.side2 = Square.side3 = Square.side4 = 5
Square.area = Square.side1 * Square.side2

#17#########################################################
# Create Random Dices  Hint: use random.randrange(min,max)
dice1 = 0
dice2 = 0

#18#########################################################
# Decrypt the following message.  Hint: We don't like numbers!
delnum = "This7is2a4scrabbled9message4that0you1have4to5take0care7of8it!"

#19#########################################################
# Decrypt the following message.  Hint: the end is the start
rtl = "?ksat ysae na egassem siht saw ?yadot uoy era woh !ajnin olleh"

#20#########################################################
# Create a decision helper Hint: use  choices.split(",")
choices = input("Write your choices separated by comma")
