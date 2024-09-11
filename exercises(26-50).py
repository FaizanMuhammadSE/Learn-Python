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