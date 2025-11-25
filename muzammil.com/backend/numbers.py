#int, float, complex

import random

integer_number = 10 #int
numbers = 1231231232443543626535

print(type(integer_number))

decimal_number = 10.5 #float
large_decimal = 3.123423432
precise_float = 0.0000004032432432

# version = 3.12.2
scientific_notation = 1.23e10 # float

complex_number1 = 2 + 3j #complex
complex_number2 = complex(4,-5) #complex
print(complex_number2)

y = 3.76
z = int(y)
print(z)

a = 5
b = float(a)
print(b)

big_int =  12312321423423423

print(random.randint(1,100)) # Random integer between 1 and 100
print(random.uniform(1.0,10.0)) # Random float between 1.0 and 10.0
print(random.choice(10,20,30,40,50)) # Random choice from a list

