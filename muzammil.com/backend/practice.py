print("Hello World!", end= " ")
print("I will print on the same line.")

x = str(3)
y = int(3)
z = float(3)
print(x)
print(y)
print(type(z))

a = 4
A = "Muzammil"
print(a)
print(A)

x,y,z = "Orange","Banana", "Cherry"
print(x)
print(y)
print(z)

m = n = o ="Orange"
print(m)
print(n)
print(o)

fruits = ["apple", "mango", "watermelon"]
a,b,c = fruits
print(a)
print(b)
print(c)

x = "Python"
y = "is"
z = "awesome"
print(x,y,z)

print(x + " " + y + " " +  z)

x = "awesome"

# Create a variable outside of a function and use it inside the function
def myfunc():
    print("Python is " + x)

myfunc()

# Create a variable inside a function, with the same name as the global variable
y = "awesome"

def myfunc2():
    y = "fantastic"
    print("Python is " + y)

myfunc2()
print("Python is " + y)
    
# If you use the global keyword, the variable belongs to the global scope

def myfunc():
    global x
    x = "fantastic"

myfunc()

print("Python is " + x)

# To change the value of a global variable insidea function,
# refer to the variable by using the global keyword

x = "awesome"

def myfunc():
    global x
    x = "fantastic"

myfunc()


print("Python is " + x)

# Import the random module, and display a random number from 1 to 9

import random

print(random.randrange(1,100))

b = "Hello, World"
print(b[-5:-2])
print(b.upper())
print(b.lower())
print(b.replace("H","J"))
print(b.split(","))

a = "Hello"
b = "World"
c = a + " " + b
print(c)

age = 32
txt = f"My name is Muzammil, I am {age}."
print(txt)

price = 59
txt = f"THe price is ${price:.2f} dollars"
print(txt)

txt = f"The price is ${20 * 59} dollars"
print(txt)

txt = "We are the so called \"Vikings\" form the north."
print(txt)

# Boolean

print(10 > 9)
print(10 < 9)
print(10 == 9)

a = 200
b = 33

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")


print(bool("Hello"))
print(bool(15))


print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

class myclass():
    def __len__(self):
        return 0

myobj = myclass()
print(bool(myobj))

def myFunction():
    return True

print(myFunction())

def myFunction():
    return True

if myFunction():
    print("YES!")
else:
    print("NO!")

x = 200
print(isinstance(x,int))
print(isinstance(x,float))
