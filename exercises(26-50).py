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

