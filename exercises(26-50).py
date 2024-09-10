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


