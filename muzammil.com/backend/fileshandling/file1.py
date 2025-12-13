import os

file = open('myexample.txt', 'w')
file.write('''Hello, World!
            this is my first file handling example.''')

file.close()
file = open('myexample.txt', 'r')
content = file.read()
print(content)

with open('myexample.txt', 'a') as file:
    file.write('\nThis line is appended to the file.')
file = open('myexample.txt', 'r')
content = file.readlines()
print(content)
#os.remove('myexample.txt')