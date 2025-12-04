#for loop in python
for i in range(5):
    print("Iteration:", i)

students = ["Alice", "Bob", "Charlie"]
for student in students:
    print("Student Name:", student)


# Using for loop with dictionary
grades = {"Alice": 90, "Bob": 85, "Charlie": 92}
for student, grade in grades.items():
    print(f"{student}: {grade}")

# Nested for loop
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")


# Using for loop with break and continue
for i in range(10):
    if i == 5:
        break  # Exit the loop when i is 5
    print(i)


for p in range(10):
    if p % 2 == 0:
        continue  # Skip even numbers
    print(p)

# Using for loop with else
for i in range(7):
    if i == 5:
        break
    print(i)
else:
    print("Loop completed without break")

for j in range(3):
    pass

#1. 

for num in range(1,11):
    print(num)

#2.

animals = ['lion','hippo','elephant','giraffe','deer']

for animal in animals:
    print(animal)

#3.

for num in range(1,21):
    if num % 2 == 0:
        print(num)

#4.

str = "Hello World"

for char in str:
    print(char)

#5.

for num in range(1,11):
    if num == 5:
        break
    else:
        print(num)