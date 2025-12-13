#try
#except
#finally
#else
#raise

"""

try:
    result = x = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

y = 5
try:
    print(y)
except NameError:
    print("Error: Variable 'y' is not defined.")
else:
    print("No errors occurred")
finally:
    print("Execution completed.")


g = "5"
g = int(g)

if g < 0:
    raise ValueError("Negative value error: your input cannot be negative.")
else:
    print("Value is acceptable.")   

#1.
"""
try:
    result = x = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

"""    

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

try:
    num1 = int(num1)
    num2 = int(num2)
    quotient = num1 / num2
    print(f"The quotient of {num1} and {num2} is {quotient}")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

#2. 
"""
try:
    file = open('unknown_file.txt', 'r')
    content = file.read()
    print(content)
    file.close()
except FileNotFoundError:
    print("Error: The file was not found.")

"""

#3.

def square_num():
    try:
        n = input("Enter a number to square: ")
        n = int(n)
        print(f"The square of {n} is {n**2}")
    except ValueError:
        print("Error: Invalid input. Please enter a valid integer.")

square_num()

#4.

def sum(a,b):
        if not isinstance(a,int) or not isinstance(b,int):
             raise TypeError("Both inputs must be integers.")
        print(a + b)
try:
    sum(5, '10')
    sum(7, 3)
    sum("Ali",8)
    sum(9,"Hamza")
    sum("Ali","Hamza")
except TypeError as te:
    print(f"TypeError: {te}")   

#5.

try:
    num_1  = input("Enter first number: ")
    num_2 = input("Enter second number: ")
    num_1 = int(num_1)    
    num_2 = int(num_2)
    print(num_1/num_2)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")    
except ValueError:
    print("Error: Invalid input. Please enter valid integers.")


"""
#6.

people = {'Muzammil':25, 'Ali':30, 'Hamza':28}
try:
    print(people['Ahmed'])
except KeyError:
    print("Error: The specified key does not exist in the dictionary.")

#7.

students = ['Tom', 'Bob', 'Mark']
try:
    print(students[5])
except IndexError:
    print("Error: List index out of range.")

#8.
class AgeError(Exception):
    """Custom exception raised for errors in the age input."""

    def __init__(self, age, message="Age must be between 18 and 60"):
        self.age = age
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        # This allows the print(e) statement to show a more descriptive error
        return f'{self.age} is an invalid age -> {self.message}'
    
def validate_age(age):
    if age < 18:
        raise AgeError(age, message="Age is below the minimum allowed limit of 18.")
    elif age > 60:
        raise AgeError(age, message="Age is above the maximum allowed limit of 60.")
    else:
        print(f"Age {age} is valid.")

# --- Test Cases ---
try:
    validate_age(35)
    validate_age(16) # This line will raise an exception and stop the try block
    validate_age(75)
except AgeError as e:
    # This block handles the first AgeError it encounters
    print(f"Caught an error: {e}")

#9.
try:
    file = open('sample.txt', 'r')
    content = file.read()
    print(content)
finally:
    if file:
        file.close()
        print(f"Ensuring sameple.txt is closed")
    else:
        print("File was not opened, so need to close")

#10.

noun = "Toronto"
try:
    noun.countvowels()
except AttributeError:
    print("Error: 'str' object has no attribute 'countvowels'.")

