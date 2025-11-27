#to store multiple items in a single variable
#sets are unordered, unindexed, and do not allow duplicate values

thisset = {'apple','banana','cherry'}
print('Original Set', thisset)
print(thisset)
print(len(thisset)) # Output: 3


# 1. 
numbers = {1,2,3,4,5}
numbers.remove(2)   
print(numbers)

# 2. 

evens = {2,4,6,8,10}
odds = {1,3,5,7,9}

print(evens.union(odds))
print(evens.intersection(odds))

# 3. 

fruits = {'apple','cherry','kiwi','banana','mango'}
print('apple' in fruits)
fruits.add('orange')
fruits.remove('cherry')
print(fruits)

# 4. 

random_words = {'table','chair','iron','calculator','pencil'}
my_list = list(random_words)
my_list.sort()
print(my_list)

# 5. 

numbers_2 = {1,2,2,3,3,4,5}
print(numbers_2)