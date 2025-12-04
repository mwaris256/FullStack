#function is a block of reusable code that performs a specific task
#it runs when it is called

def my_first_function():
    return "this is my first function"

print(my_first_function())

my_first_function()


my_first_function()

def my_function():
    pass

my_function()

def greet(name):
    print(f"hello {name}")

greet("muzzammil")
greet("waris")
greet("ali")

#argument is a information that is passed into a function
#argument vs parameter
#parameter is the variable listed inside the parentheses in the function definition
#argument is the value that is sent to the function when it is called


#default parameter
def greet(name="guest"):
    print(f"hello {name}")

greet()
greet("muzzammil")

#this is key value argument
def my_pet(pet_name, pet_type="cat"):
    print(f"i have a {pet_type} named {pet_name}")

my_pet("fluffy")
my_pet("mitho", "parrot")

#positional argument
def my_pet2(pet_name, pet_type):
    print(f"i have a {pet_type} named {pet_name}")

my_pet2("dog", "bruno")
my_pet2(pet_type="bruno", pet_name="dog") #this will give wrong output because of positional argument, in this case we redefine here 

#Arbitrary Arguments *args
def my_friends(*friends):
    print("my friends are:")
    for friend in friends:
        print(friend)


my_friends("ali", "umer", "ahmed", "saad", "hamza")


def my_freind_circle(greeting, *friends):
    for friend in friends:
        print(f"{greeting}, {friend} in my circle")


my_freind_circle("salam", "ali", "umer", "ahmed")


def loop_function(*numbers):
    total = 0
    for num in numbers:
        total += num 
    return total

print(loop_function(10,20,30,40,50))


#arbitrary keyword arguments **kwargs

def my_details(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

my_details(name="muzzammil", age=25, city="karachi")

#function scope
x = 10  #global variable
def my_scope():
    global y 
    y = 5  #local variable
    print(f"inside function: x={x}, y={y}")

my_scope()
print(y)

def outer_function():
    outer_var = "i am outside!"
    
    def inner_function():
        inner_var = "i am inside!"
        print(outer_var)
        print(inner_var)
    
    inner_function()

outer_function()


#nonlocal keyword, for the variables bolongs outer function

def outer():
    var = "outer variable"
    
    def inner():
        nonlocal var
        var = "inner variable"
        print("inner:", var)
    
    inner()
    print("outer:", var)

outer()

#LEGB rule Local, Enclosing, Global, Built-in
x = "global x"
def outer_func():
    x = "enclosing x"
    
    def inner_func():
        x = "local x"
        print(x)
    
    inner_func()
    print(x)

outer_func()
print(x)


#Decorators
#a decorator is a function that takes another function as an argument, 
# extends its behavior without modifying it, and returns a new function

def change_case(func):
   def inner():
    return func().upper()
   return inner

@change_case #decorator syntax
def say_hello():
    return "hello world"

print(say_hello())


#Lambda Functions
#anonymous function
#used for short period of time

add = lambda a, b: a + b
print(add(5, 10))

def mymath(n):
    return lambda a: a * n

double = mymath(2)
print(double(10))

#recursive function

def countdown(n):
    if n <= 0:
        print("blastoff!")
    else:
        print(n)
        countdown(n-1)

countdown(5)

#Generators
#generators are functions that return an iterable set of items,
#one at a time, in a special way using the yield keyword
#pause and resume their state between each item

def my_generator():
    yield 1
    yield 2
    yield 3

for value in my_generator():
    print(value)

#1.

def greet(name):
    print(f"Hello {name}")

greet("Muzammil")

#2. 

def square(n):
    print(n**2)

square(5)
square(7)

#3. 

def calculate_sum(a,b,c):
    print(a+b+c)

calculate_sum(2,6,4)
calculate_sum(10,13,23)

#4. 

def introduce(name,age=18):
    print(f"Name: {name}, Age: {age}")

introduce("Tom")
introduce("Muzammil",32)

#5.

def is_even(n):
    if n % 2 == 0:
        print(True)
    else:
        print(False)

is_even(8)
is_even(11)

#6.

def find_max(a,b,c):
    if a > b and a > c:
        print(a)
    elif b > a and b > c:
        print(b)
    else:
        print(c)

find_max(10,3,7)
find_max(6,22,12)
find_max(8,33,45)

#7.

def is_palindrome(s):
    if s == s[::-1]:
        print(True)
    else:
        print(False)

is_palindrome("mother")
is_palindrome("noon")
is_palindrome("civic")

#8.

def count_vowels(s):
    count = 0
    vowels = ['a','e','i','o','u']
    for char in s:
        if char in vowels:
            count += 1
    print(count)

count_vowels("Muzammil") 
count_vowels("bear")
count_vowels("beautiful") 

#9.

def factorial(n):
    total = n
    for num in range(n-1,0,-1):
        total = total * num
    print(total)

factorial(5)
factorial(6)

#10.

def sum_list(list):
    total = 0
    for num in list:
        total += num
    print(total)

sum_list([1,2,3,4,5])

#11. 


#add = lambda a, b: a + b
#print(add(5, 10))

#def mymath(n):
 #   return lambda a: a * n

#double = mymath(2)
#print(double(10))

multiply = lambda a,b : a*b
print(multiply(6,7))

#12. 

people = [("Tom",25),("Bob", 30),("Mark",28),("Nick",15)]
people.sort(key=lambda person: person[1])

print(people)

#13. 

numbers = [1,2,3,4,5,6,7,8,9,10]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

#14.

squared = list(map(lambda x: x**2, numbers))
print(squared)

#15.

get_string_lengths = lambda string_list : list(map(len,string_list))

print(get_string_lengths(['table','cat','father']))

#16.


#def countdown(n):
 #   if n <= 0:
  #      print("blastoff!")
   # else:
    #    print(n)
     #   countdown(n-1)

def factorial_recursive(n):
    if n == 0:
        return 1
    elif n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    else:
        return (n * factorial_recursive( n - 1))
            
print(factorial_recursive(6))
print(factorial_recursive(5))

#17.

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)
    
print(fibonacci(6))
print(fibonacci(7))

#18.

def sum_digits(n):
    if n < 10:
        return n
    else:
        return (n % 10) + sum_digits(n // 10)
    
print(sum_digits(12345))

#19. 

def power(x,n):
    if x == 0:
        return 0
    if n == 0:
        return 1
    else:
        return x * power(x,n-1)
    
print(power(3,3))
print(power(5,3))

#20.

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
    
print(gcd(28,21))
print(gcd(10,15))
     