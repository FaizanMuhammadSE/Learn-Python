from pprint import pprint
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

##################################### Exercise #10 (Sequence Item Picking)
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


##################################### Exercise#11
# Generate List having items 1 to 20
# Expected Output [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# Range returns ranges object, to convert it into List, we have to use list function
print([i for i in range(1,21)])
# or
print(list(range(1,21)))



##################################### Exercise#12
# Complete the script so that it produces the expected output. Please use my_range  as input data.
# my_range = range(1, 21)
# Expected_Output [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]
my_range = range(1, 21)
print([i*10 for i in my_range])

#################################### Exercise#13
# Complete the script, so it generates the expected output using my_range  as input data. Please note that the items of the expected list output are all strings.
# my_range = range(1, 21)
#  Expected output: 
# ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']  
my_range = range(1,21)
print([str(i) for i in my_range])
#or
print(list(map(str,my_range))) # map built-in func of python applies a function to iterable object

##################################### Exercise#14
# Remove duplicates from List
a = ['1',1,'1',1,2]
print(list(set(a))) # Set don't allow duplicates, and we can convert back set into list and vice-versa, but set don't maintain order of list

# or
# To maintain order of list we can use OrdererdDictionary
from collections import OrderedDict
a = ["1", 1, "1", 2]
a = list(OrderedDict.fromkeys(a))
print(a)

# or by looping

################################## Exercise#15 (Create Dictoinary)
dictionary = {"a": 1, "b": 2}
# or
dictionary2 = dict(a = 100, b = 200)
print(dictionary["a"], dictionary["b"])
print(dictionary2["a"], dictionary["b"])


################################# Exercise#16 (Access Dictionary Item)
# Please complete the script so that it prints out the value of key b .
d = {"a": 1, "b": 2}
print(d["b"])
# or
print(d.get("b"))

################################# Exercise#17 (Access Dictionary Item)
# Calculate the sum of the values of keys a  and b .
# d = {"a": 1, "b": 2, "c": 3}
# Expected output: 
# 3
d = {"a": 1, "b": 2, "c": 3}
print(d["a"] + d["b"])


################################# Exercise#18 (KeyError)
# d = {"Name": "John", "Surname": "Smith"}
# print(d["Smith"])
# Answer: 
# There is no key Smith  in the dictionary. Smith  is a value. You want to use Surname  if you want to access Smith :


################################# Exercise#19 (Add Key in Dict)
# Add a new pair of key (e.g. c ) and value (e.g. 3 ) to the dictionary and print out the new dictionary.

# d = {"a": 1, "b": 2}
# Expected output:  {'a': 1, 'c': 3, 'b': 2} 
d = {"a": 1, "b": 2}
d["c"] = 3
print(d)


################################# Exercise#20 (Sum of dict values)
# Calculate the sum of all dictionary values.

# d = {"a": 1, "b": 2, "c": 3}
# Expected output: 6 

d = {"a": 1, "b": 2, "c": 3}
# d.values()  returns a list-like dict_values  object while the sum  function calculates the sum of the dict_values  items.
print(sum(d.values()))

################################ Exercise#21 (Dictionary Filtering)
# Question: Filter the dictionary by removing all items with a value of greater than 1.
# d = {"a": 1, "b": 2, "c": 3}
# Expected output: {'a': 1}  
d = {"a": 1, "b": 2, "c": 3}
res = {}
for x,y in d.items():
    if y <= 1:
        res[x]=y
print(res)

# or
# by using dictionary comprehension
d = {"a": 1, "b": 2, "c": 3}
d = {x:y for x,y in d.items() if y <= 1}
# or
# by using dictionary constructor
d = dict((key, value) for key, value in d.items() if value <= 1)
print(d)

################################ Exercise#22 (Formatted Print a dictory having lists)
# Create a dictionary and print it out.
d = {"a": [x for x in range(1,11)], "b": [x for x in range(11,21)], "c": [x for x in range(21,31)]}
# or
# d = {"a": list(range(1,11)), "b": list(range(11,21)), "c": list(range(21,31))}
# using f-string
formatted_output = f'{{"a": {d["a"]},\n "b": {d["b"]},\n "c": {d["c"]}}}'
print(formatted_output)
# or
# pprint is used to print dictionary in formatted way
pprint(d)

################################ Exercise#23 (Multi Level Indexing)
# Question: Access the third value of key b  from the dictionary.
# d = dict(a = list(range(1, 11)), b = list(range(11, 21)), c = list(range(21, 31)))
# Expected output: 13  
d = dict(a = list(range(1, 11)), b = list(range(11, 21)), c = list(range(21, 31)))
print(d["b"][2])


################################ Exercise#24 (Iterate Dictionary)
# Question: Please complete the script so that it prints out the expected output.

# d = dict(a = list(range(1, 11)), b = list(range(11, 21)), c = list(range(21, 31)))
# Expected output: 

# b has value [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# c has value [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
# a has value [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

d = dict(a = list(range(1, 11)), b = list(range(11, 21)), c = list(range(21, 31)))
for x,y in d.items():
    print(f'{x} has value {y}')


################################ Exercise#25 (print a to z)
for i in range(97,123):
    print(chr(i))