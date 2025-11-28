# Tuple = () ordered and unchangeable, Duplicates OK. FASTER
#Store multiple items in a single variable
#Tuple is ordered, unchangeable and allows duplicate values

my_tuple = (1,2,3,4,5,"apple","banana","cherry", 5.98, True, None, ('book','pen','computer'))
print('Original Typle:', my_tuple)

print(len(my_tuple)) # Output: 12
my_fruit = tuple(('apple','banana','cherry')) # Creating a tuple using the tuple() constructor
print("fruit Tuple", my_fruit)

# 1. 

my_tuple2 = ('Mississauga',"Brampton", "Toronto","Milton", "Hamilton")
print(my_tuple2[0])
print(my_tuple2[-1])

# 2. 
animals = ('Lion','Fox','Bear','Giraffe','Wolf','Sheep')
print(animals[2])
print(animals[4])
print(animals.index('Fox',0,-1))

# 3. 

numbers = [10,20,30,40]
print(numbers[0] + numbers[2])
print(numbers[1] * numbers[3])

# 4. 

countries = ('Canada','Pakistan','Australia','England','South Africa','Sri Lanka')
print(countries[:2])
print(countries[4:])

# Practice

fruits = ('apple','orange','banana','coconut','coconut')

print(fruits.index("orange"))
print(fruits.count("coconut"))

for fruit in fruits:
    print(fruit)