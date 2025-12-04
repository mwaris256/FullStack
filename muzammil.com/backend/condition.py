#condition if else , elif , nested if else 


a = 40
b = 50
if a > b:
    print("a is greater than b")
elif a == b:
    print("a is equal to b")
    print("b is equal to a")
else:
    print("b is greater than a")


marks = 85
if marks >= 90:
    print("Grade: AA")
elif marks >= 80:
    print("Grade: A+")
elif marks >= 70:
    print("Grade: A")
elif marks >= 60:
    print("Grade: B")
elif marks >= 50:   
    print("Grade: C")
else:
    print("Grade: F")

#nested if else
num = 16
if num > 0:
    if num % 2 == 0:
        print("The number is positive and even.")
    else:
        print("The number is positive and odd.")
else:
    print("The number is not positive.")

#short hand if else
age = 10
print("Adult") if age >= 18 else print("Minor")


#with logicaL operators
x = -100
if x > 0 and x < 50:
    print("x is a positive number less than 50")


if x < 0 or x > 100:
    print("x is either negative or greater than 100")

if not(x >= 0):
    print("x is a negative number")

#1.

num = -20
if num > 0:
    print("The number is positive")
elif num == 0:
    print("The number is zero")
else:
    print("The number is negative")

#2. 

colors = ['blue','black','green','orange','purple']
if 'red' in colors:
    print("Red is in the list of colors")
else:
    print("No, red is not in the list of colors")

#3.

num1 = 12
num2 = 12

if num1 > num2:
    print(num1)
elif num2 > num1:
    print(num2)
else:
    print("The numbers are equal")

#4.

num = 1

if num > 10 and num < 50:
    print("The number is between 10 and 50")
elif num > 50:
    print("The number is greater than 50")
else:
    print("The number is less than 10")

#5. 

num = 7
print("Even") if num % 2 == 0 else print("Odd")

#6.

mark = 95

if mark > 90:
    print("A")
elif mark >= 80 and mark <= 89:
    print("B")
elif mark >= 70 and mark <= 79:
    print("C")
else:
    print("Fail")

#7.

str = "Muzammil"
if "e" in str:
    print("Yes, the string contains the letter e")
else:
    print("No, the string does not contain the letter e")

#8.

age = 19

if age >= 18:
    if age >= 21:
        print("You are eligible for a special program")
    else:
        print("You are not eligible")
else:
    print("You are not eligible")

#9.

num1 = 37
num2 = 37

if num1 > num2:
    print("First is larger")
elif num2 > num1:
    print("Second is larger")
else:
    print("Both are equal")

#10. 

num1 = 25
num2 = 3

if num1 * num2 > 100:
    print("The product of the two numbers is greater than 100.")
else:
    print("No the product of the two numbers is not greater than 100.")