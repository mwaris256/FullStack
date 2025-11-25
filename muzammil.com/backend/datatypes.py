name = "Muzammil" #str
print(type(name))

age = 30 # int
print(type(age))

height = 5.9 # float
print(type(height))

is_student = False # bool
print(type(is_student))

fruits = ['apple','banana','cherry'] #list
print(type(fruits))

person = {"name": 'Muzammil', age: 30} # dict
print(type(person))

numbers = (1,2,3) # tuple
print(type(numbers))

unique_numbers = {1,2,3} # set
print(type(unique_numbers))

data = None #NoneType
print(type(data))

file_data = b'Hello World!' #bytes
print(type(file_data))

byte_array = bytearray(b'Hello') #bytearray
print(type(byte_array))

memory_view = memoryview(b"Hello") #memoryview


#1.

name = "Jack"
print(type(name))

age = 30
print(type(age))

number = 3.8
print(type(number))

is_Friday = False
print(type(is_Friday))


#2.

str = "123"
a = int(str)
print(a)

b = float(str)
print(b)

#c = str(a)
#print(c)

#3. 

a = 10
b = 5
print(a+b)
print(a-b)
print(a*b)
print(a/b)

#4. 

z = 3.9
m = 2
g = complex(4,-5)
print(m + z)
print(g * z)
print(z - m)

#5.

x = 6
y = 7.8
print(x==y)
print(x!=y)
print(x >= y)

#6.

quote = "Our greatest weakness lies in giving up"
print(quote[:6])
print(quote[-4:])
print(quote[-1:])

#7. 

j = 25
k = 3
print(j + k)
print(k - j)
print(j * k)
print(j/k)
print(j % k)

#8.

name = 'muzammil'
print(name.capitalize())
print("a" in name)
name2 = name.replace("m","W",1)
print(name2)

#9.

f = 50.8
s = 8
print(f*s)
print(float(f/s))
print(s**f)

