# to store multiple items in a single variable
# dictionaries are ordered (as of Python 3.7), changeable, and do not allow duplicate keys
# key: value pairs

thisdict = {
    'brand: Ford',
    'model: Mustand',
    'year: 1964'
}

print('Original Dictionary', thisdict)
print(len(thisdict)) # Output: 3
print(thisdict) # Accessing value by key

# 1. 

students = {'Tom':32, "Mark": 26, "Bob": 28}
students['Nick'] = 18

print(students)

# 2. 

countries = {"Canada": "Ottawa", "Pakistan": "Islamabad", "India": "Delhi", "USA": "Washington Dc", "England": "Manchester"}
countries['England'] = 'London'

print(countries)

# 3. 

products = {"Dell Laptop": 800, "Printer": 70, "Dining Table": 250, "Iron" : 80}
print(products)

products['Notebook'] = 15

print(products)

# 4. 

phonebook = {'Muzammil' : '6479018962', "Waris": 4168971367, "Homephone": 9058558962}
phonebook["Ali"] = 6478171478

print(phonebook)

# 5. 

subjects = {'Math': 90, "History": 82, "Science": 80}
print("Math" in subjects)

subjects['Math'] = 95
print(subjects)

# 6. 

fav_color = {'Muzammil' : 'Blue', "Tim": "Red", "Mike": "Brown", "Sam" : 'White' }
print(fav_color.keys())
print(fav_color.values())

# 7. 

employees = {'Mike':600000, "Phil": 70000, "Tom" : 80000}
for key,value in employees.items():
    print(f'Name : {key}, Salary: {value}')



