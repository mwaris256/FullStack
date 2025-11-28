# List = [] ordered and changeable. Duplicates are OK
# Set = {} unordered and immutable, Add/Remove OK. No Duplicates
# Tuple = () ordered and unchangeable, Duplicates OK. FASTER

# Lists are used to store multiple items in a single variable
# Lists are ordered, changeable, and allows duplicate values 

my_list = [1,2,3,4,5, 'apple','banana','cherry',5.98,True, None, ['book','pen','computer']]
print("Original List:", my_list)

print(len(my_list)) # Output: 12

myfruit = list(('apple', 'banana', 'cherry')) # Creating a list using the list() consturctor
print("fruits List:", myfruit)

# 1. 

fruits_1 = ["apple","banana","mango","watermelon","kiwi","pear"]
fruits_1.pop()
fruits_1.remove('banana')
print(fruits_1)

# 2.

numbers = [1,2,3,4,5,6,7,8]
print(numbers[-1])
numbers[1] = 100
print(numbers)

# 3. 

numbers_2 = [10,20,30,40,50,60,70]
numbers_2.pop(2)
print(numbers_2)
numbers_2.append(90)
print(numbers_2)
numbers_2.remove(40)
print(numbers_2)

# 4. 

my_string = "Programming"
print(my_string[3:8])
print(my_string[5])
print(my_string[:5])

# 5. 

int_list = [10,20,30,40,50,60]
print(int_list[0] + int_list[-1])
print(int_list[1] - int_list[3])
print(int_list[1] * 2)

# 6. 

my_string2 = "The best player in the world is Ronaldo."
print(my_string2.find('e'))
print(my_string2.lower())
print(my_string2.split(" "))


# Practice

fruits = ['apple','orange','banana','watermelon','mango']

print(fruits)
print(fruits[2])
print(fruits[3])
print(fruits[0:3])
print(fruits[::2])
print(fruits[::-1])

for fruit in fruits:
    print(fruit)

print(len(fruits))
print("apple" in fruits)
print("pineapple" in fruits)

fruits[0] = 'pineapple'

for fruit in fruits:
    print(fruit)

fruits.append("grapes")
fruits.remove("orange")
fruits.insert(2,'plum')
fruits.sort()
fruits.reverse()
print(fruits.index('mango'))
print(fruits.count("banana"))
print(fruits)

letters = ['a','b','c']
matrix = [[0,1],[2,3]]
zeros = [0]*10
print(zeros)
combined = zeros + letters
print(combined)
numbers = list(range(20))
print(numbers)
print(numbers[::2])

chars = list("Hello World")
print(chars)
print(len(chars))

numbers_2 = [1,2,3]
first = numbers_2[0]
second = numbers_2[1]
third = numbers_2[2]

for letter in enumerate(letters):
    print(letter)

for letter in enumerate(letters):
    print(letter[0],letter[1])

letters.append('d')
print(letters)