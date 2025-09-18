'''
Four pillars of OOP?

1.Encapsulation → Wrapping data & methods together.

2.Abstraction → Hiding implementation details, showing only necessary features.

3.Inheritance → One class inherits properties of another.

4.Polymorphism → One name, many forms (method overriding/overloading).
'''
#Classes and objects in python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

my_car = Car("Toyota", "Corolla")  # Object
print(my_car.brand)  # Toyota

#__init__ in Python-A special constructor method that runs when an object is created.Used to initialize object properties.

#Example of Inheritance
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):  # Inheritance
    def speak(self):
        print("Dog barks")

dog = Dog()
dog.speak()  # Dog barks

#Method Overidding-Same method name in parent & child, but child changes behavior.
class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet(self):
        print("Hello from Child")

obj = Child()
obj.greet()  # Hello from Child

