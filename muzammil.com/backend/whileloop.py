#while loop for when condition is true
i = 0
while i < 5:
    print("Iteration:", i)
    i += 1

students = ["Alice", "Bob", "Charlie"]
index = 0
while index < len(students):
    print("Student Name:", students[index])
    index += 1

# Using while loop with dictionary
grades = {"Alice": 90, "Bob": 85, "Charlie": 92}
keys = list(grades.keys())
index = 0
while index < len(keys):
    student = keys[index]
    grade = grades[student]
    print(f"{student}: {grade}")
    index += 1

# Nested while loop
i = 0
while i < 3:
    j = 0
    while j < 2:
        print(f"i: {i}, j: {j}")
        j += 1
    i += 1 

# Using while loop with break and continue
i = 0
while i < 10:
    if i == 5:
        break  # Exit the loop when i is 5
    print(i)
    i += 1

p = 0
while p < 10:
    if p % 2 == 0:
        p += 1
        continue  # Skip even numbers
    print(p)
    p += 1

#6.

i = 1
while i < 6:
    print(i)
    i += 1

#7.

number = 0 

while number <= 50:
    try:
        user_input = input("Please enter a number: ")
        number = int(user_input)
        if number <= 50:
            print(f'{number} is not greater than 50. Please try again.')
    except ValueError:
        print("Invalid input. Please enter a valid number.")

print(f"You enter {number}, which is greater than 50. The loop has ended.")

#8.

i = 10
while i > 0:
    print(i)
    i -= 1

#9. 

i = 1
while i < 10:
    if i == 7:
        break
    else:
        print(i)
    i += 1

#10. 

num = 0
while num <= 0:
    try:
        user_inputt = input("Please enter a number: ")
        num = int(user_inputt)
        if num <= 0:
            print(f"{num} is not a positive number. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid number")

print(f"You entered {num}, which is a positive number. The loop has ended.")