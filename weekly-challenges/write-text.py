import os

# Create a program that stores data in a text file.

line_1 = input()
line_2 = input()
line_3 = input()

# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))
# Join the current directory with the filename
file_path = os.path.join(current_dir, 'textFile.txt')

# open file
file = open(file_path, 'wt')
file.write(line_1)
file.write('\n-------------\n')
file.write(line_2)
file.write('\n-------------\n')
file.write(line_3)
file.close()