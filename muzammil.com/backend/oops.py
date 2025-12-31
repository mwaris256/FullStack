#object oriented programming system
#Class, Object, Attributes, methods, Inheritance, Encapsulation, Polymorphism, Abstraction, constructor 

#class is a blueprint for creating objects
#object is an instance of a class
#attributes are the properties/data of an object
#methods are behaviors/functions of an object

#inheritance is a mechanism where a new class inherits properties and behaviors from an existing class child and parent class
#protect data using private variables and methods
#polymorphism is the ability to take many forms method overloading and overriding: same method but diffrent behavior
#abstraction is the process of hiding complex implementation details and showing only the essential features of an object

#contructor is a special method that is called when an object is instantiated

from abc import ABC, abstractmethod

class Employee:
    def __init__(self, emp_id, name, position, salary): #constructor
        self.emp_id = emp_id
        self.name = name
        self.position = position
        self.salary = salary

    def display_info(self): #method
        print(f"Employee ID: {self.emp_id}, Name: {self.name}, Position: {self.position}, Salary: {self.salary}")

class Manager(Employee): #inheritance
    def __init__(self, emp_id, name, position, salary, department):
        super().__init__(emp_id, name, position, salary) #calling parent constructor
        self.__department = department #private attribute

    def display_info(self): #method overriding
        super().display_info()
        print(f"Department: {self.__department}")


#creating objects
emp1 = Employee(101, "Alice", "Developer", 70000) #instance of Employee class
emp1.display_info()
mgr1 = Manager(201, "Bob", "Manager", 90000, "IT") #instance of Manager class
mgr1.display_info()


class Student:
    def __init__(self, student_id, name, major, marks):
        self.student_id = student_id
        self.name = name
        self.major = major
        self.__marks = marks  #private attribute

    def display_info(self):
        print(f"Student ID: {self.student_id}, Name: {self.name}, Major: {self.major}")
    def get_marks(self):  #encapsulation
        return self.__marks
    def set_marks(self, marks):
        self.__marks = marks

class GraduateStudent(Student): #inheritance
    def __init__(self, student_id, name, major, research_topic):
        super().__init__(student_id, name, major)
        self.research_topic = research_topic

    def display_info(self): #method overriding
        super().display_info()
        print(f"Research Topic: {self.research_topic}") 

    #encapsulation
    def set_research_topic(self, topic):
        self.research_topic = topic
    def get_research_topic(self):
        return self.research_topic
    


class Person(ABC): #abstraction
    @abstractmethod
    def get_details(self):
        pass

class Teacher(Person):
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def get_details(self):
        return f"Teacher Name: {self.name}, Subject: {self.subject}"

class StudentPerson(Person):
    def __init__(self, student_id, name, grade):
        self.student_id = student_id
        self.name = name
        self.grade = grade

    def get_details(self):
        return f"Student ID: {self.student_id}, Name: {self.name}, Grade: {self.grade}"
    
#1.

class Car:
    def __init__(self, color):
        self.color = color

    def get_details(self):
        return f"Color: {self.color}"

colorful_car = Car("Red")
print(colorful_car.get_details())
    

#2,3,13

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

    def __str__(self):
        print (f"Person(Name: {self.name}, Age: {self.age})")

person1 = Person("John",30)
person1.display_info()
person2 = Person("Ali",25)
person2.display_info()
person1.greet()
person2.greet()
person1.__str__()
person2.__str__()

#4. 

class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author

    def get_summary(self):
        print(f"{self.title}' is written by {self.author}.")

book1 = Book("1984","George Orwell")
book1.get_summary()
book2 = Book("To Kill a Mockingbird","Harper Lee")
book2.get_summary()

#5,6,8,19

class Account:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance= amount
        print(f"Deposited: {amount}. New balance: {self.__balance}")

        return self

    def withdraw(self,amount):
        if amount > self.__balance:       

            print("Insufficient funds.")
        else:
            self.__balance -= amount
            print(f"Withdrew: {amount}. New balance: {self.__balance}")
        
        return self

    def get_balance(self):
        return self.__balance
    
    def convert_currency(self, rate):
        return self.__balance * rate
    


account1 = Account(1000)
account1.deposit(500)
account1.withdraw(200)
account1.withdraw(2000)

account2 = Account(2000)
account2.deposit(1000).withdraw(500).withdraw(300)

#7.

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"  

dog1 = Dog("Buddy")
print(f"{dog1.name} says {dog1.speak()}")

#9.

class Employee:
    company_name = "Stackpole"

    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name

    def get_company(self):
        return Employee.company_name
    
emp1 = Employee(1, "Nick")
print(f"{emp1.name} works at {emp1.get_company()}")

#11.

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius
    
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

square1 = Square(4)
print(f"Area of square: {square1.area()}")

circle1 = Circle(5)
print(f"Area of circle: {circle1.area()}")

#14.

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        print(f"Make: {self.make}, Model: {self.model}")

class Car(Vehicle):
    def __init__(self, make, model, num_doors):
        super().__init__(make, model)
        self.num_doors = num_doors

    def display_info(self):
        super().display_info()
        print(f"Number of doors: {self.num_doors}")

car1 = Car("Toyota", "Camry", 4)
car1.display_info()

class ElectricCar(Car):
    def __init__(self, make, model, num_doors, battery_capacity):
        super().__init__(make, model, num_doors)
        self.battery_capacity = battery_capacity

    def display_info(self):
        super().display_info()
        print(f"Battery Capacity: {self.battery_capacity} kWh")

electric_car1 = ElectricCar("Tesla", "Model S", 4, 100)
electric_car1.display_info()

#15

class Engine:
    """Represents a car engine."""
    def __init__(self, cylinders, horsepower):
        self.cylinders = cylinders
        self.horsepower = horsepower

    def start(self):
        """Simulates starting the engine."""
        return f"Engine ({self.cylinders} cylinders, {self.horsepower}hp) started."

    def __str__(self):
        return f"{self.cylinders}-cylinder engine with {self.horsepower} hp"

class Car:
    """
    Represents a car, demonstrating aggregation by using 
    an instance of Engine as an attribute.
    """
    def __init__(self, make, model, engine):
        self.make = make
        self.model = model
        # Aggregation: Car has an Engine, but the Engine can exist 
        # independently of the Car.
        self.engine = engine 

    def drive(self):
        """Simulates driving the car."""
        # We can call methods of the aggregated object (engine)
        engine_status = self.engine.start()
        return f"The {self.make} {self.model} is driving. {engine_status}"

    def __str__(self):
        return f"{self.make} {self.model} with {self.engine}"

# --- Example Usage ---

# 1. Create an independent Engine instance
v6_engine = Engine(cylinders=6, horsepower=300)

# 2. Create a Car instance and pass the existing Engine instance to it
my_car = Car(make="Toyota", model="Camry", engine=v6_engine)

# 3. Use the Car object
print(my_car)
print(my_car.drive())

print("-" * 20)

# Demonstrate the independent existence:
# Even if 'my_car' is deleted or goes out of scope, 'v6_engine' still exists.
del my_car 
print(f"The engine still exists independently: {v6_engine.start()}")


#16.
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        for book in self.books:
            print(f"Title: {book.title}, Author: {book.author}")

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

library = Library()
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book2 = Book("1984", "George Orwell")
library.add_book(book1)
library.add_book(book2)
library.display_books()

#17.

class Appliance(ABC):
    @abstractmethod
    def turn_on(self):
        pass

class WashingMachine(Appliance):
    def turn_on(self):
        return "Washing Machine is now ON."

class Refrigerator(Appliance):
    def turn_on(self):
        return "Refrigerator is now ON."
    
washing_machine = WashingMachine()
print(washing_machine.turn_on())

refrigerator = Refrigerator()
print(refrigerator.turn_on())

#18.

class Playable(ABC):
    @abstractmethod
    def play(self):
        pass

class Guitar(Playable):
    def play(self):
        return "Strumming the guitar!"
    
guitar = Guitar()
print(guitar.play())

class Piano(Playable):
    def play(self):
        return "Playing the piano!"
    
piano = Piano()
print(piano.play())
