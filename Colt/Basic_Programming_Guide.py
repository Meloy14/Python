# ----------------------------------------------------------------------------------------
# Sample 01: Escape Sequence Practice
# ----------------------------------------------------------------------------------------
message = "hello\nyou"
print(message) # Output: hello
               #        you
mountains = "/\\/\\/\\" # Output: /\/\/\
print(mountains)
quotation = "hi \"there\""
print(quotation) # Output: hi "there"

# ----------------------------------------------------------------------------------------
# Sample 02: Formatting Strings
# ----------------------------------------------------------------------------------------
first = "Colt"
last = "Steele"
formatted1 = "First Name: {}, Last Name: {}".format(first, last)
formatted2 = f"First Name: {first}, Last Name: {last}"
print(formatted1) # Output: First Name: Colt, Last Name: Steele
print(formatted2) # Output: First Name: Colt, Last Name: Steele

# ----------------------------------------------------------------------------------------
# Sample 03: Getting User Input
# ----------------------------------------------------------------------------------------
print("What's your favorite color?")
# favColor = input()
# print(f"You said {favColor}")

# ----------------------------------------------------------------------------------------
# Sample 04: Random and IF-Else Sample.
# ----------------------------------------------------------------------------------------
from random import randint
num = randint(1, 1000) #picks random number from 1-1000
if (num%2) == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")

from random import choice
food = choice(['apple','grape', 'bacon', 'steak', 'worm', 'dirt'])
if food == "apple" or food == "grape":
    print("fruit")
elif food == "bacon" or food == "steak":
    print("meat")
elif food == "worm" or food == "dirt":
    print("yuck")

# ----------------------------------------------------------------------------------------
# Sample 05: For Loop and Range Exercise
# ----------------------------------------------------------------------------------------
x = 0
for ctr in range(11,20,2): # Iterate by 2, Range is from 11 to 20
    x += ctr
print(f"Total number is {x}")

number = 0 # store random number in here, each time through
i = 0  # i should be incremented by one each iteration
while number != 5:
    number = randint(1, 10)
    i += 1
print(f"Stop at {number}")

# ----------------------------------------------------------------------------------------
# Sample 06: Creating Lists
# ----------------------------------------------------------------------------------------
my_stuff = ["hello", 2, 1.5, True] # List contanins string and float
nums = list(range(1,100)) # List 1 to 99 using Range() function

swap_value = ["James", "Michelle"]
swap_value[0], swap_value[1] = swap_value[1], swap_value[0]

# ----------------------------------------------------------------------------------------
# Sample 07: Accessing List Data
# Change "Hanna" to "Hannah" (there should be an 'h' at the end)
# Change "Geoffrey" to "Jeffrey"
# Change "aparna" to "Aparna" (capitalize it)
# ----------------------------------------------------------------------------------------
people = ["Hanna","Louisa","Claudia", "Angela","Geoffrey", "aparna"]
#Change "Hanna" to "Hannah"
Hannah = people.index("Hanna")
people[Hannah] = "Hannah"
#Change "Geoffrey" to "Jeffrey"
Jeffrey = people.index("Geoffrey")
people[Jeffrey] = "Jeffrey"
#Change "aparna" to "Aparna" (capitalize it)
Aparna = people.index("aparna")
people[Aparna] = "Aparna"

# ----------------------------------------------------------------------------------------
# Sample 08: List Iteration Exercise
# sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"] 

# Write code that loops over the list and adds all the strings together to form one large 
# combined string (don't add any spaces between them) 
# The combined string should be in all UPPERCASE as well 
# Save the result in a variable called result  
# ----------------------------------------------------------------------------------------
sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]
result = ""
for i in sounds:
    result += i
result = result.upper()

# ----------------------------------------------------------------------------------------
# Sample 09: Lists Methods
# ----------------------------------------------------------------------------------------
instructors = []
# Add "Sam" to instructors list
instructors.append("Sam")
# Add the following strings to the instructors list 
instructors.extend(["Colt", "Blue", "Lisa"])
# Remove the last value in the list
instructors.pop()
# Remove the first value in the list
instructors.remove("Sam")
# Add the string "Done" to the beginning of the list
instructors.insert(0, "Done")
print(f"Instructors: {instructors}")

# ----------------------------------------------------------------------------------------
# Sample 10: List Comprehension
# Given a list ["Elie", "Tim", "Matt"], create a variable called answer, which is a new list
# containing the first letter of each name in the list.  I would use a list comprehension,
# though you could also loop over manually.
# Given a list [1,2,3,4,5,6], create a new variable called answer2, which is a new list of
# all the even values.  Another good candidate for a list comp.
# ----------------------------------------------------------------------------------------
names10 = ["Elie", "Time", "Matt"]
answer = [nans[0] for nans in names10]
print(f"Sample 10: {answer}") # Output: Sample 10: ['E', 'T', 'M']
myNum = [1,2,3,4,5,6]
answer2 = [nans2 for nans2 in myNum if nans2%2 == 0]
print(f"Sample 10: {answer2}") # Output: Sample 10: [2, 4, 6]

# ----------------------------------------------------------------------------------------
# Sample 11: More List Comprehension
# 1. Given two lists [1,2,3,4] and [3,4,5,6], create a variable called answer3, which is a
# new list that is the intersection of the two. Your output should be [3,4] .  Hint: use the
# in  operator to test whether an element is in a list. 
# For example:  5 in [1,5,2]  is True.  3 in [1,5,2]  is False.
# 2. Given a list of words ["Elie", "Tim", "Matt"] create a variable called answer4, which
# is a new list with each word reversed and in lower case (use a slice to do the reversal!)
# Your output should be ['eile', 'mit', 'ttam']
# ----------------------------------------------------------------------------------------
answer3 = [val for val in [1,2,3,4] if val in [3,4,5,6]]
print(f"Sample 11: {answer3}")
answer4 = [val[::-1].lower() for val in ["Elie", "Tim", "Matt"]]
print(f"Sample 11: {answer4}")

# ----------------------------------------------------------------------------------------
# Sample 12: Another List Comprehension
# For all the numbers between 1 and 100(including 100), create a variable called answer5, which
# contains a list with all the numbers that are divisible by 12.  (12, 24, etc)
# USE A LIST COMPREHENSION.
# ----------------------------------------------------------------------------------------
answer5 =  [nAns for nAns in range(1,101) if nAns%12 == 0]
print(f"Sample 12: {answer5}")

# ----------------------------------------------------------------------------------------
# Sample 13: Another List Comprehension
# Given the string "amazing", create a variable called answer6, which is a list containing all
# the letters from "amazing" but not the vowels (a, e, i, o, and u).
# The answer should look like: ['m', 'z', 'n', 'g'].
# Use a list comprehension!
# ----------------------------------------------------------------------------------------
answer6 = [nAns for nAns in "amazing" if nAns not in "aeiou"]
print(f"Sample 13: {answer6}")

# ----------------------------------------------------------------------------------------
# Sample 14: Nested List Comprehension
# Using a nested list comprehension and range(), create a variable called answer7  with the
# following value - [[0, 1, 2], [0, 1, 2], [0, 1, 2]] .  To break it down...start by using
# range and a list comp to generate the list [0,1,2].  And then repeat that whole thing 3
# times in a nested list comp.  It's all a bit tricky to discuss, so maybe it's just best to
# look at the solution if you get stuck.  
# ----------------------------------------------------------------------------------------
answer7 = [[x for x in range(0,3)] for nAns in range(0,3)]
print(f"Sample 14: {answer7}")

# ----------------------------------------------------------------------------------------
# Sample 15: One More Nested List Comp
# Using list comprehension, create a variable called answer with the following value :
# [
#  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#  ]
# it's a 10x10 nested list.  10 rows, each row contains the numbers 0-9.   Don't worry about
# the formatting/spacing, I just added a bunch of returns to make things clearer. Your answer will
# be all on one giant line. Use nested list comprehension and range() to accomplish this.
# ----------------------------------------------------------------------------------------
answer6 = [[x for x in range(0,10)] for nAns in range(0,10)]
print(f"Sample 15: {answer6}")

# ----------------------------------------------------------------------------------------
# Python Functions
#   Slicing:
# some_list[start:end:step]
# ----------------------------------------------------------------------------------------

# First parameter for slice: start
first_list = [1, 2, 3, 4]
print(f"Slicing Start: {first_list[1:]}") # Output: Slicing Start: [2, 3, 4]
print(f"Slicing Start: {first_list[3:]}") # Output: Slicing Start: [4]
# If you enter a negative number, it will start the slice that many back from the end
print(f"Slicing Start: {first_list[-1:]}") # Output: Slicing Start: [4]
print(f"Slicing Start: {first_list[-3:]}") # Output: Output: Slicing Start: [2, 3, 4]

# Second parameter for slice: end
second_list = [1, 2, 3, 4]
print(f"Slicing Start: {second_list[:2]}") # Output: Slicing Start: [1, 2]
print(f"Slicing Start: {second_list[:4]}") # Output: Slicing Start: [1, 2, 3, 4]
print(f"Slicing Start: {second_list[1:3]}") # Output: Slicing Start: [2, 3]
print(f"Slicing Start: {second_list[:-1]}") # Output: Slicing Start: [1, 2, 3]
print(f"Slicing Start: {second_list[1:-1]}") # Output: Slicing Start: [2, 3]

# Third parameter for slice: step
third_list = [1, 2, 3, 4, 5, 6]
print(f"Slicing Start: {third_list[1::2]}") # Output: Slicing Start: [2, 4, 6]
print(f"Slicing Start: {third_list[::2]}") # Output: Slicing Start: [1, 3, 5]
# With negative numbers, reverse the order
print(f"Slicing Start: {third_list[1::-1]}") # Output: Slicing Start: [2, 1]
print(f"Slicing Start: {third_list[:1:-1]}") # Output: Slicing Start: [6, 5, 4, 3]
print(f"Slicing Start: {third_list[2::-1]}") # Output: Slicing Start: [3, 2, 1]
# Reversing lists / strings
string_rev = "This is fun!"
print(f"Reverse: {string_rev[::-1]}") # Output: Reverse: !nuf si sihT
# Modifying portions of lists
numbers_mod = [1, 2, 3, 4, 5]
numbers_mod[1:3] = ['1', 'b', 'c']
print(f"Mod Mid: {numbers_mod}") # Output: Mod Mid: [1, '1', 'b', 'c', 4, 5]