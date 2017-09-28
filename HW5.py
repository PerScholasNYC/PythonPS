#Prints the question
print("How many seconds are there in 42 minutes 42 seconds?")
#creates a function
def time():
    #creates a vaariable for seconds
    seconds = (42 * 60)
    #prints the solution of variable and 42
    print(seconds + 42 )
#calls on funtion
time()
#prints the question
print("How many miles are there in 10 kilometers?")
#creates function
def distance():
    #creates variable
    mile = 1.61
    #prints solution
    print(10 / mile)
#calls on function
distance()

#prints the question
print("How much is 83 degress Fahrenheit in degree celsius?")
#creates variables
subtract = 32
multiply = 5 / 9
#prints results
print (f"83 degrees celsius is {subtract * multiply}")

#imports math library
import math
#prints request
print ("Find the square root for the following 81, 19, 16, and 121")
#creates variable
x = int(input())
##creates if else statement
if x == 81:
    print (math.sqrt(81))

elif x == 19:
    print (math.sqrt(19))

elif x == 16:
    print (math.sqrt(16))

elif x == 121:
    print (math.sqrt(121))


#import math library
import math
#prints request
print("Find the area of a circle that has a radius of 9")
#creates variables
R = math.pow(9, 2)
Pi = 3.14
#print results
print(Pi * R)

#write a boolean function that returns true or false if the letter a,e,i,o,u and in a string provided by the user
#creates global variable
i = input()
#creates function
def connie(str):
    #creates local variable
    has_x= False
    #creates for loop
    for x in i:
        #creates if statement
        if x == 'x':
            has_x= True
    if has_x == True:
        #returns the value
        return True
        #else statement
    else:
        #returns the value
        return False
#prints results
print(f"This is {connie(i)}")


i = input()
def letter(str):
    vowel = False
    for x in str:
        if x == 'a' or 'e' or 'i' or 'o' or 'u':
            print("switch to true")
            vowel = True
        else:
            vowel = False
    if vowel == True:
        return True
    else:
        return False


print(f"{letter(i)}")

#import math library
import math
#prints question
print("What is the volume of a sphere with radius of 5?")
#creates function
def sphere():
    #creates variables
    i = 4 / 3
    x = 3.14
    y = math.pow(5, 3)
    #print results
    print(i * x * y)
#calls functin
sphere()

9

#import datetime library
import datetime
#create variable
today = datetime.datetime.now()
#print result
print(f"The current date and time is {today}")

#import datetime library
import datetime
#creates variable
today = datetime.datetime.now()
#prints results
print(f"The current year is {today.year}")

#import collections library
from collections import Counter
#creates function
def letter():
    #creates variables
    word = input()
    counter = Counter(word)
    #print results
    print(counter['a'])

#creates variable
word = input("Type a word to count the number of letters in it: ")
#prints results
print(len(word))

#creates variable
i = 20
#creates while loop
while (i > 0):
    #print results
   print(i)
   i = i - 1

#print request
print("Type a number:")
#create variable
n = int(input())
#creates if and else statment
if n % 2 == 0:
    print("You typed an Even number")
else:
    print("You typed an Odd number")

#create variable
length = 0
#creates for loop
for x in input("Type something: "):
    length += 1
    #print results
print(f"The length of your string is {length}")

#creates for loop
for x in input("Just type something and watch the magic: "):
    #print results
    print (x)'''
