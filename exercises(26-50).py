import os
################################ Exercise#26
# Question: Make a script that prints out numbers from 1 to 10

# Expected output:

# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
for i in range(10):
    print(i+1)


################################### Exercise#27 (Create a function)
# Question: 
# Create a function that calculates acceleration given initial velocity v1, final velocity v2, start time t1, and end time t2. The formula for acceleration is:
# a = (v2-v1)/(t2-t1)

# To test your solution, call the function by inputting values 0, 10, 0, 20 for v1, v2, t1, and t2, respectively, and you should get the expected output.

# Expected output: 0.5

def findAccelration(v1,v2,t1,t2):
    # If you were creating this in Python 2, the solution would need to have float functions converting the two differences to float numbers 
    # because if the differences are integers, Python will also output an integer (e.g., 3 / 2 outputs 0). 
    # But In Python 3, you don't have to convert to floats.
    return (v2-v1)/(t2-t1)

print(findAccelration(0,10,0,20))


################################## Exercise#28 (Type Error)
# Question:  Why is there an error in the code, and how would you fix it?
# def foo(a, b):
#     print(a + b) 
# x = foo(2, 3) * 10
# Reason: function isnt returning, so return something


################################## Exercise#29 (Volume)
# Please write a function that calculates liquid volume in a sphere using the following formula. The radius r  is always 10, so consider making it a default parameter.
from math import pi as PI
def volume(h,r=10):
    return (4*PI*pow(r,3))/3 - (PI*pow(h,2)*(3*r-h))/3
    # or
    # return (4 * PI * r**3) / 3 - (PI * h**2 * (3 * r - h)) / 3
print(volume(2))    


################################## Exercise#30 (Arguments)
# Question:  Why do you get an error, and how would you fix it?
# def foo(a=2, b):
#     return a + b

# Reason: Always put non-default parameters first, followed by default ones.


################################ Exercise#31(Function Blueprint)
# Question:  Why is there an error in the code, and how would you fix it?

# def foo(a=1, b=2):
#     return a + b
 
# x = foo - 1
# Reason: foo is a function, and you need to call it with parentheses.

################################ Exercise#32(Global Variable)
# Question:  What will the following script output? Please try to do this by mind if you can.

# c = 1
# def foo():
#     return c
# c = 3
# print(foo())
# Reason: At the time when the function is called c  has a value of 3


################################ Exercise#33(local Variable)
# Question:  Here's another similar exercise. What will the following script output? Try to do this mentally if you can.

# c = 1
# def foo():
#     c = 2
#     return c
# c = 3
# print(foo())
# Output: 2
# ReNote that c  is a local variable that exists only inside the function. The other two c  variables are global variables and have nothing to do with the function
# If you want to refer to global variable inside function while updating then use global keyword infront of variable inside function

################################ Exercise#34(Local Vs Global Variable)
# Question: The following script throws a NameError  in the last line saying that c  is not defined. Please fix the function so that there is no error and the  last line can print out the value of c  (i.e. 1 ).

# def foo(): 
#     c = 1 
#     return c 
# foo() 
# print(c)
# Expected output: 1
def foo():
    global c # By using global keyword with variable inside function we can make it Global instead of local to func
    c = 1 
    return c 
foo() 
print(c)

################################# Exercise#35 (string splitter)
# Create a function that takes any string as input and returns the number of words for that string.
def findWords(sentence):
    return len(sentence.split(" "))

inputLine = input()
print(findWords(inputLine))

################################ Exercise#36 (Word Counter)
def wordCounter(fileName):
    # Get the current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Join the current directory with the filename
    file_path = os.path.join(current_dir, f'./supporting-files/{fileName}')
    file = open(file_path, 'rt')
    content = file.read()
    print(len(content.split(" ")))

wordCounter('words1.txt')


################################ Exercise#37 (Advanced Word Counter)
#NOte: There can be some commas separated words instead of space

def advancedWordCounter(fileName):
    # Get the current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Join the current directory with the filename
    file_path = os.path.join(current_dir, f'./supporting-files/{fileName}')
    file = open(file_path, 'rt')
    content = file.read()
    fixedContent = content.replace(',', ' ')
    print(len(fixedContent.split(" ")))

advancedWordCounter('words2.txt')


################################ Exercise#38 (Name Error)
# math.sqrt(9)
# Reason: math module isn't imported

################################ Exercise#39 (Attribute Error)
import math
# print(math.cosine(1)) # Reason: There is no cosine function in math module
print(math.cos(1))

################################ Exercise#40 (Type Error)
# Please try to guess what is missing in the following code and add the missing part so that the code works fine.
import math
# print(math.pow(2)) # Reason: pow func take 2 arguments
print(math.pow(2,3))

################################ Exercise#41 (Letters in File)
# Create a script that generates a text file with all letters of the English alphabet inside it, one letter per line.

def generateAlphabets(fileName):
    # Get the current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Join the current directory with the filename
    file_path = os.path.join(current_dir, f'./supporting-files/{fileName}')
    file = open(file_path, 'wt')
    for i in range(97,123):
        file.write(chr(i) + "\n")
    file.close()

generateAlphabets('alphabets.txt')

################################ Exercise#42 (Iterating Multiple Sequence)
# Print out in each line the sum of homologous items of the two sequences.

a = [1, 2, 3]
b = (4, 5, 6)

for i in range(max(len(a),len(b))):
    print(a[i] + b[i])

# or
# Using the zip function to iterate over both sequences simultaneously
# The zip function takes iterables (can be zero or more), aggregates them in a tuple, and returns it. 
# This is useful for iterating over multiple sequences in parallel.
for x, y in zip(a, b):
    print(x + y)
