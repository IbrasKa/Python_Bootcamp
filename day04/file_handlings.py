# THIS ONLY WORKS FOR READING, WRITING AND DELETING .TXT FILES.

# Reading a file
import os

path = "/Users/iy811/PycharmProjects/Python_Bootcamp/day04/files/Test.txt"

text_file = open(path, 'r')

print(text_file.read())

text_file.close()

"""
print(text_file.readline())
print(text_file.readline())
print(text_file.readline())
"""

print('-------------Writing a file--------------------------')

path = 'files/Test2.txt'

text_file2 = open (path, 'w')

text_file2.write('This is a new text file\nPython created this file')

text_file2 = open(path, 'r')

print(text_file2.read())

text_file2.close()

print('-------------Deleting a file--------------------------')

os.remove(path)
