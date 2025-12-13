import mymodule1 as mm1
from mymodule1 import person, address
import platform
from datetime import datetime , date, timedelta
import math as m
import json #convert from json to python dict and vice versa
#from pandas import DataFrame as pd #pip Python install Packages
#import CamelCase
from greetings import say_hello
import math_operations as mt
import text_utils as tu
import formatter as fr
import constants 
from calculator import addition, subtraction


print("Sum is:", mm1.add(5, 7))

print("Python Version:", platform.python_version())
#print(dir(platform))

print("Person Details:", person["age"], address)


print("Current Date and Time:", datetime.now())

year = datetime.now().year
print("Current Year:", year) #20251209074220486930

#strftime
now = datetime.now()
formatted_date = now.strftime("%c")
print("Formatted Date and Time:", formatted_date)

print(m.sqrt(81))
print(m.factorial(6))
print(m.pi)
print(m.ceil(4.2))
print(m.floor(4.8))
print(m.pow(2, 5))


myjson = '{"name": "Muzzammil", "age": 25, "city": "Karachi"}'

py_dict = json.loads(myjson)
print("Converted Python Dictionary:", py_dict)
new_json = json.dumps(py_dict)
print("Converted JSON String:", new_json)

#Creating a DataFrame
data = {
    "Name": ["Muzzammil", "Ali", "Ayesha"],
    "Age": [25, 30, 22],
    "City": ["Karachi", "Lahore", "Islamabad"]
}   
#df = pd.DataFrame(data)
#print("DataFrame:\n", df)


#cc = CamelCase()
#txt = "hello world from muzzammil"
#print("CamelCase Text:", cc.hump(txt))

#1. 
print("Greeting:", say_hello())

#2.

print("Addition:", mt.add(10,5))
print("Subtraction:", mt.subtract(10,5))
print("Multiplication:", mt.multiply(10,5))
print("Division:", mt.divide(10,5))

#3. 

print("Vowel Count:", tu.count_vowels("Hello World from Muzzammil"))
print("Vowel Count:", tu.count_vowels("This is a sample text"))

#4. 

print("Capitalized Text:", fr.capitalize_words("hello world from muzzammil"))

#19.

print("Value of PI:", constants.PI)

#Math 

#6. 

print("Factorial of 5:", m.factorial(5))

#7.
print("Square Root of 64:", m.sqrt(64))

#8.

def angle_in_radians(degrees):
    return f"Sine: {m.sin(m.radians(degrees))} Cosine: {m.cos(m.radians(degrees))}"

print("45 degrees in radians:", angle_in_radians(45))
print("90 degrees in radians:", angle_in_radians(90))

#9.

print("5 to the power of 3:", m.pow(5,3))

#10.

numbers = [4, 16, 25, 36, 49]
print("Log of numbers:", [m.log(num) for num in numbers])

#Datetime

#11.

print("Current Date and Time:", datetime.now())

#12. 

def days_until_new_year():
    today = datetime.now()
    next_new_year = datetime(today.year + 1, 1 , 1, 0,0,0)
    time_difference = next_new_year - today
    return time_difference.days

print("Days until New Year:", days_until_new_year())

#13.

def convert_date_string_to_datetime(date_string: str) -> datetime:

    return datetime.strptime(date_string, "%Y-%m-%d")

date_str = "2024-12-08"
datetime_obj = convert_date_string_to_datetime(date_str)
print(f"The date string '{date_str}' converted to a datetime object is {datetime_obj}")
print(f"Type of the converted object: {type(datetime_obj)}")

#14.

def calculate_age_year(birth_year : int) -> int:
    current_age_year = datetime.now().year
    return current_age_year - birth_year

print("Age for birth year 1993:", calculate_age_year(1993))

def calculate_age_full(birth_date: str) -> int:
    birth_datetime = datetime.strptime(birth_date, "%Y-%m-%d")
    today = datetime.now()
    age = today.year - birth_datetime.year
    if (today.month, today.day) < (birth_datetime.month, birth_datetime.day):
        age -= 1
    return age

print("Full Age for birth date 1993-12-25:", calculate_age_full("1993-12-25"))

#15.

current_date = date.today()

days_to_add = 30

future_date = current_date + timedelta(days=days_to_add)

print(f"Current Date: {current_date}, Date after {days_to_add} days: {future_date}")


#Packages

#22.

print("Addition using calculator package:", addition.add(30, 10))
print("Subtraction using calculator package:", subtraction.subtract(30, 10))
