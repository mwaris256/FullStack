myCountry = "I live in Pakistan"
print(myCountry)

myName = "Muzammil"
print(myName)

myName2 = ""
print(myName2)

text = """This is a multi-line string
It can span multiple lines
You can write a paragraph here"""

print(text)

#string as array
print(myName[0]) # first character
print(myName[1]) # second character

print(len(myName))
for char in myName:
    print(char)

print('write' in text)

print("hello" + " " "world")

if "Muzammil" in myName:
    print("Yes", "Muzammil is found in myName")
else:
    print("No, 'Muzammil' is not found in myName")

print(myName.upper())

myName2 = "Python Programming"
print(myName[-8:]) #Slicing from index 0 to 5

myName3 = " Hello World "
print(myName3.strip()) #Remove whitespace from both ends

print(myName3.lower()) #convert to lowercase
print(myName3.upper()) #convert to uppercase

print(myName3.replace("H", "J")) #Replace 'H' with 'J'

p= (myName3.split(",")) #Split the string at each space
print(type(p))

h = "Hello"
w = "World"
greeting = h + ' ' + w #Concatenate strings with a space in between
print(greeting)

age = 25
intro = 'my age is ' + str(age)
print(intro) 

#formatting f-string

introf = f'My name is {myName} and I am {age} years old'
print(introf)

#1. 

fname = "Muzammil Waris"
print(len(fname))

print(fname[0])
print(fname[-1])

m = 'hello world'
print(m.upper())

z = 'PYTHON'
print(z.lower())

a = "Hello"
b = "World"
c = (a + " "+ b)
print(c)

print(c[6:])
phrase = "This is a bad day"
print(phrase.replace("bad","good"))

z = "Hi"
print(z*5)

q = "This is a test. It is fun"
print(q.count("is"))

i = "I love Python programming"
print("Python" in i)

b = " Python "
print(b.strip())

word = 'hi'
print(word.center(10))

num = "5"
print(num.zfill(3))

num2 = "7"
print(num2.ljust(3,'0'))

my_string = "hello world, welcome"
print(my_string.find('world'))

my_string2 = "This is a test. It is fun"
print(my_string2.rfind("is"))

my_string3 = "Learning.py"
print(my_string3.endswith(".py"))

my_string4 = "Python3"
print(my_string4.startswith("Py"))

fruits2 = "apple,banana,orange"
fruits_list = fruits2.split()
print(fruits_list)

languages = ["HTML", "CSS", "JS"]
print("-".join(languages))