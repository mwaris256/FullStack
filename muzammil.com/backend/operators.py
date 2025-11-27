#arithmetic operators
#assignment operators
#comparison operators
#logical operators
#bitwise operators
#identity operators
#membership operators

# Arithemetic Operators
a  = 10
b = 3
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a/b)
print("Floor Division:", a//b)
print("Modulus", a % b)
print("Exponentiation", a ** b)


# Assignment Operators
c = 5
d = 8
c += d # c = c + d , 13
c -= d # c = c - d, 5
c *= d # c = c * d, 40
c /= d # c = c / d, 5.0
c %= d # c = c % d, 5.0
print("c after operations:", c)


f = 7
g = 10
f %= g # f = f % g
print('f after modulus operation', f) # 7

# Comparison Operators
x = 15
y = 20
print('Equal', x == y)
print("Not Equal", x != y)
print("Greater Than", x > y)
print("Less Than", x < y)
print("Greater Than or Equal To", x >= y)
print("Less Than or Equal To", x <= y)

# Logical Operators
p = True
q = False
print("AND", p and q)
print("OR", p or q)
print("NOT p", not p)

# Bitwise Operators
m = 5
n = 3 
print("Bitwise AND", m & n)
print("Bitwise OR", m | n)

# Identity Operators
list1 = [1,2,3]
list2 = list1
list3 = [1,2,3]
print('list1 is list2', list1 is list2)
print('list1 is list3', list1 is list3)
print('list1 is not list3', list1 is not list3)
