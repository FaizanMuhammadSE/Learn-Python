######################################### Exercise#1 (Variable Updating)
# What will the following code produce?
a = 2
a = 4
a = 6
print(a+a+a) # it will print 18

######################################### Exercise#2 (Naming Rules)
# What's wrong with the following script?
# a = 1 => Fine
# _a = 2 => Fine
# _a2 = 3 => Fine
# 2a = 4 => Wrong (variable name can be start with numeric)

######################################## Exercise#3 (Compare Vs Assing)
# Executing the code will throw an error. Can you explain why?
# a = 1
# b = 2
# print(a == b)
# print(b == c) #Error c isn't defined

######################################## Exercise#4 (Type Error)
# Fix the last line so that it outputs the sum of 1 and 2. Please do not change the first two lines, only the last one.
# a = "1"
# b = 2
# print(a + b)
# Expected output: 3 
a = "1"
b = 2
print(int(a) + b)

####################################### Exercise#5 (Sequence Indexing)
# Complete the script so that it prints out the second item of the list.
# letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
# Expected output: 
# b
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
print(letters[1])

####################################### Exercise#6 (Sequence Slicing)
# Please complete the script so that it prints out a list slice containing items d , e , and f .
# letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
# Expected output: 
# ['d', 'e', 'f']
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
print(letters[3:6])

###################################### Exercise #7
# Complete the script to print out the first three items of the list 'letters'.
# letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
# Expected output:
# ['a', 'b', 'c']

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
print(letters[:3])


##################################### Exercise #8
# Complete the script so that it prints out the letter 'i' using negative indexing.
# letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
# Expected output:
# i
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
print(letters[-2])


##################################### Exercise #9
# Complete the script so that it prints out a list slice containing the last three items of the list letters .
# letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
# Expected output:
# ['h', 'i', 'j']
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
print(letters[-3:])

##################################### Exercise #10
# Complete the script so that it prints out a list slice containing letters a, c, e, g, and i. 
# letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
# Expected output: 
# ['a', 'c', 'e', 'g', 'i']
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
res = []
for i in range(len(letters)):
    if i%2 == 0:
        res.append(letters[i])
print(res)
# Through List Slicing
# The complete syntax of list slicing is [start:end:step].
# When you don't pass a step, Python assumes the step is 1.
# [:]  itself means to get everything from start to end.
# So, [::2]  means get everything from start to end at a step of two.
print(letters[::2])


