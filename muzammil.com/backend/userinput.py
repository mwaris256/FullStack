import math

#print("what is you name?: ")
#name = input()
#print(f"Hello, {name}!")

#father_name = input("What is your father's name?: ")
#print(f"Hello, Mr. {father_name}!")


#fav_book = input("What is your favorite book?: ")
#fav2_book = input("What is your second favorite book?: ")
#fav3_book = input("What is your third favorite book?: ")
#print(f"Do you know? Your favorite books are {fav_book}, {fav2_book}, and {fav3_book}!")

"""
try:
    x = input("Enter a number to squareroot: ")
    x = int(x)
    if x < 0 or x == 0 or x is None or x == 1:
        raise ValueError("The value must be greater than one.")
    else:
        x = math.sqrt(x)
        x = round(x)
        print(f"The square root of your number is: {x}")
except ValueError as ve:
    print(f"ValueError: {ve}")

#1. 

print("what is your favorite color?: ")
fav_color = input()
print(f"Your favourite color is {fav_color}!")

#2. 

try:    
    birth_year = (input("What year were you born in ? "))
    birth_year = int(birth_year)
    age = 2025 - birth_year
    print(f"You are {age} years old")
    
except ValueError:
    print(f"Invalid input. Please enter a integer.")

#3. 

try:
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    num1 = int(num1)
    num2 = int(num2)
    product = num1 * num2
    print(f"The product of {num1} and {num2} is {product}") 

except ValueError:
    print("Invalid input. Please enter integers only.")



#4.

name = input("Please enter your name: ")
preferred_greeting = input("Hi or Hello: ")
if preferred_greeting.lower() == "hi":
    print(f"Hi, {name}!")
elif preferred_greeting.lower() == "hello":
    print(f"Hello, {name}!")

"""

#5.

shopping_list = []
while input != "done":
    shopping_items = input("Enter an item to add to your shopping list (or type 'done' to finish): ")
    shopping_list.append(shopping_items)
    if shopping_items.lower() == "done":
        break
print("These are the items in your shopping list: ")
for item in shopping_list:
            print(f"{item}")